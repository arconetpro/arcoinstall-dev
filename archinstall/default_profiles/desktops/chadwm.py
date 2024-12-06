import shutil
import archinstall

from typing import TYPE_CHECKING, override
from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile
from archinstall.lib.models import User

if TYPE_CHECKING:
	from archinstall.lib.installer import Installer


class ChadwmProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__("Chadwm", ProfileType.WindowMgr, description='')

	@property
	def packages(self) -> list[str]:
		# return super().packages + [
		return [
			'a-candy-beauty-icon-theme-git',
			'alacritty',
			'arandr',
			'arc-gtk-theme',
			'archlinux-logout-git',
			'archlinux-tweak-tool-git',
			'arcolinux-alacritty-git',
			'arcolinux-app-glade-git',
			'arcolinux-arc-dawn-git',
			'arcolinux-btop-git',
			'arcolinux-chadwm-git',
			'arcolinux-chadwm-pacman-hook-git',
			'arcolinux-fastfetch-git',
			'arcolinux-gtk-surfn-arc-git',
			'arcolinux-hblock-git',
			'arcolinux-keyring',
			'arcolinux-local-xfce4-git',
			'arcolinux-mirrorlist-git',
			'arcolinux-nlogout-git',
			'arcolinux-pacman-git',
			'arcolinux-paru-git',
			'arcolinux-powermenu-git',
			'arcolinux-rofi-git',
			'arcolinux-rofi-themes-git',
			'arcolinux-root-git',
			'arconet-variety-config',
			'arconet-wallpapers',
			'arconet-xfce',
			'autorandr',
			'bash-completion',
			'bat',
			'bibata-cursor-theme-bin',
			'btop',
			'dash',
			'dmenu',
			'duf',
			'eww',
			'fastfetch-git',
			'feh',
			'firefox',
			'gcc',
			'git',
			'gitahead-git',
			'gvfs',
			'gvfs-dnssd',
			'gvfs-smb',
			'lolcat',
			'lxappearance',
			'make',
			'meld',
			'mkinitcpio-firmware',
			'neofetch',
			'nomacs-qt6-git',
			'numlockx',
			'paru-git',
			'pavucontrol',
			'picom-git',
			'playerctl',
			'polkit-gnome',
			'ripgrep',
			'rofi-lbonn-wayland',
			'sparklines-git',
			'sublime-text-4',
			'surfn-icons-git',
			'sxhkd',
			'thunar',
			'thunar-archive-plugin',
			'thunar-volman',
			'ttf-hack',
			'ttf-jetbrains-mono-nerd',
			'ttf-meslo-nerd-font-powerlevel10k',
			'variety',
			'volumeicon',
			'xdg-desktop-portal',
			'xdg-user-dirs',
			'xfce4-appfinder',
			'xfce4-notifyd',
			'xfce4-power-manager',
			'xfce4-screenshooter',
			'xfce4-settings',
			'xfce4-taskmanager',
			'xfce4-terminal',
			'xorg-xsetroot',
			'yay-git',
		]

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
