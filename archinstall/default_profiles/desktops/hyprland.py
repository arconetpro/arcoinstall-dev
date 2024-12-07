import shutil

import archinstall
from typing import TYPE_CHECKING, override

from archinstall.default_profiles.profile import GreeterType, ProfileType, SelectResult
from archinstall.default_profiles.xorg import XorgProfile
from archinstall.lib.models import User
from archinstall.default_profiles.desktops import SeatAccess
from archinstall.tui import Alignment, FrameProperties, MenuItem, MenuItemGroup, ResultType, SelectMenu

if TYPE_CHECKING:
	from archinstall.lib.installer import Installer


if TYPE_CHECKING:
	from collections.abc import Callable

	from archinstall.lib.translationhandler import DeferredTranslation

	_: Callable[[str], DeferredTranslation]


class HyprlandProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('Hyprland', ProfileType.DesktopEnv, description='')

		self.custom_settings = {'seat_access': None}

	@property
	@override
	def packages(self) -> list[str]:
		return [
			"wofi",
			"qt5-wayland",
			"qt6-wayland",
			"grim",
			"slurp"
			] + [
			'a-candy-beauty-icon-theme-git',
			'alacritty',
			'arc-gtk-theme',
			'arcolinux-alacritty-git',
			'arcolinux-app-glade-git',
			'arcolinux-btop-git',
			'arcolinux-config-all-desktops-git',
			'arcolinux-dconf-all-desktops-git',
			'arcolinux-fastfetch-git',
			'arcolinux-gtk-surfn-arc-git',
			'arcolinux-keyring',
			'arcolinux-mirrorlist-git',
			'arcolinux-pacman-git',
			'arcolinux-paru-git',
			'arcolinux-root-git',
			'arconet-variety-config',
			'arconet-wallpapers',
			'avahi',
			'bat',
			'bash-completion',
			'bibata-cursor-theme-bin',
			'btop',
			'downgrade',
			'duf',
			'expac',
			'fastfetch-git',
			'feh',
			'firefox',
			'git',
			'gvfs',
			'gvfs-dnssd',
			'gvfs-smb',
			'hw-probe',
			'man-db',
			'man-pages',
			'mkinitcpio-firmware',
			'mlocate',
			'mintstick-git',
			'most',
			'neofetch',
			'noto-fonts',
			'paru-git',
			'rate-mirrors-bin',
			'ripgrep',
			'sofirem-git',
			'sublime-text-4',
			'surfn-icons-git',
			'ttf-hack',
			'variety',
			'wget',
			'xdg-desktop-portal',
			'xdg-user-dirs',
			'yay-git',
			] + [
			'archlinux-logout-git',
			'archlinux-tweak-tool-git',
			'arcolinux-hyprland-git',
			'arcolinux-kitty-git',
			'arcolinux-powermenu-git',
			'arcolinux-pywal-cache-git',
			'arcolinux-rofi-git',
			'arcolinux-rofi-themes-git',
			'arcolinux-wayland-app-hooks-git',
			'arconet-xfce',
			'file-roller',
			'grim',
			'hyprcursor-git',
			'hyprland-git',
			'kitty',
			'lxappearance',
			'mako',
			'micro',
			'numlockx',
			'pamixer',
			'pavucontrol',
			'picom-git',
			'polkit-gnome',
			'pulsemixer',
			'rofi-lbonn-wayland',
			'swaybg',
			'thunar',
			'thunar-archive-plugin',
			'thunar-volman',
			'ttf-jetbrains-mono-nerd',
			'waybar-git',
			'wofi',
			'xfce4-terminal',
		]

	@property
	@override
	def services(self) -> list[str]:
		if pref := self.custom_settings.get('seat_access', None):
			return [pref]
		return []

	def _ask_seat_access(self) -> None:
		# need to activate seat service and add to seat group
		header = str(_('Sway needs access to your seat (collection of hardware devices i.e. keyboard, mouse, etc)'))
		header += '\n' + str(_('Choose an option to give Sway access to your hardware')) + '\n'

		items = [MenuItem(s.value, value=s) for s in SeatAccess]
		group = MenuItemGroup(items, sort_items=True)

		default = self.custom_settings.get('seat_access', None)
		group.set_default_by_value(default)

		result = SelectMenu(
			group,
			header=header,
			allow_skip=False,
			frame=FrameProperties.min(str(_('Seat access'))),
			alignment=Alignment.CENTER
		).run()

		if result.type_ == ResultType.Selection:
			if result.item() is not None:
				self.custom_settings['seat_access'] = result.get_value().value

	@override
	def do_on_select(self) -> SelectResult | None:
		self._ask_seat_access()
		return None

	@override
	def post_install(self, install_session: 'Installer') -> None:
		users: User | list[User] = archinstall.arguments.get('!users', [])
		if not isinstance(users, list):
			users = [users]

		for user in users:
			source = install_session.target / "etc" / "skel"
			destination = install_session.target / "home" / user.username

			try:
				shutil.copytree(source, destination, dirs_exist_ok=True)
				install_session.arch_chroot(f'chown -R {user.username}:{user.username} /home/{user.username}')
				print(f"Copied {source} to {destination}")
			except Exception as e:
				print(f"Error copying configuration: {e}")

	@property
	@override
	def default_greeter_type(self) -> GreeterType | None:
		return GreeterType.Sddm
