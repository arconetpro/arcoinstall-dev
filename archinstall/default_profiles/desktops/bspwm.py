import shutil

import archinstall
from typing import TYPE_CHECKING, override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile
from archinstall.lib.models import User

if TYPE_CHECKING:
	from archinstall.lib.installer import Installer


class BspwmProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('Bspwm', ProfileType.WindowMgr, description='')

	@property
	@override
	def packages(self) -> list[str]:
		# return super().packages + [
		return [
			'bspwm',
			'sxhkd',
			'dmenu',
			'xdo',
			'rxvt-unicode'
			] + [
			'a-candy-beauty-icon-theme-git',
			'alacritty',
			'arc-gtk-theme',
			'arcolinux-alacritty-git',
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
			'bash-completion',
			'bibata-cursor-theme-bin',
			'fastfetch-git',
			'feh',
			'firefox',
			'git',
			'gvfs',
			'gvfs-dnssd',
			'gvfs-smb',
			'mkinitcpio-firmware',
			'neofetch',
			'noto-fonts',
			'paru-git',
			'ripgrep',
			'surfn-icons-git',
			'ttf-hack',
			'variety',
			'xdg-desktop-portal',
			'xdg-user-dirs',
			'yay-git',
			] + [
			'arandr',
			'archlinux-logout-git',
			'archlinux-tweak-tool-git',
			'arcolinux-bspwm-git',
			'arcolinux-polybar-git',
			'arcolinux-powermenu-git',
			'arcolinux-rofi-git',
			'arcolinux-rofi-themes-git',
			'arcolinux-volumeicon-git',
			'arconet-xfce',
			'awesome-terminal-fonts',
			'dmenu',
			'file-roller',
			'lxappearance',
			'numlockx',
			'pavucontrol',
			'picom-git',
			'polkit-gnome',
			'polybar',
			'arcolinux-polybar-git',
			'rofi-lbonn-wayland',
			'sutils-git',
			'thunar',
			'thunar-archive-plugin',
			'thunar-volman',
			'volumeicon',
			'xfce4-notifyd',
			'xfce4-power-manager',
			'xfce4-screenshooter',
			'xfce4-taskmanager',
			'xfce4-terminal',
			'xtitle-git',
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
