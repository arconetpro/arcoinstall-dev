import shutil
import archinstall

from typing import TYPE_CHECKING, override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile

from archinstall.lib.models.users import User
if TYPE_CHECKING:
	from archinstall.lib.installer import Installer


class WayfireProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__(
			"Wayfire",
			ProfileType.WindowMgr,
			description="Wayfire is a 3D Wayland compositor",
		)

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
			'arcoinstall-pacman-git',
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
			'man-db',
			'man-pages',
			'mkinitcpio-firmware',
			'plocate',
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
			'yad',
			'yay-git',
			] + [
			'arcoinstall-system-config-git',
			'archlinux-logout-git',
			'archlinux-tweak-tool-git',
			'arcolinux-foot-git',
			'arcolinux-kitty-git',
			'arcolinux-powermenu-git',
			'arcolinux-pywal-cache-git',
			'arcolinux-rofi-git',
			'arcolinux-rofi-themes-git',
			'arcolinux-wallpapers-wayfire-git',
			'arcolinux-wayfire-git',
			'arcolinux-wayland-app-hooks-git',
			'arconet-xfce',
			'dex',
			'file-roller',
			'foot',
			'kitty',
			'lxappearance',
			'mako',
			'micro',
			'numlockx',
			'pamixer',
			'pavucontrol',
			'polkit-gnome',
			'pulsemixer',
			'python-pywal',
			'rofi-lbonn-wayland',
			'swaybg',
			'swayidle',
			'swaylock',
			'swww',
			'thunar',
			'thunar-archive-plugin',
			'thunar-volman',
			'ttf-jetbrains-mono-nerd',
			'ttf-meslo-nerd-font-powerlevel10k',
			'waybar-git',
			'wayfire-git',
			'wayfire-plugins-extra-git',
			'wcm-git',
			'wf-kill-git',
			'wf-shell-git',
			'wl-clipboard',
			'xfce4-terminal',
		] + [
			'arcolinux-sddm-simplicity-git',
		]
		
	@override
	def post_install(self, install_session: 'Installer') -> None:
		from archinstall.lib.args import arch_config_handler
		users: list[User] | None = arch_config_handler.config.users

		if not users:
		    return

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
