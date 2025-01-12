import shutil

import archinstall
from typing import TYPE_CHECKING, override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile
from archinstall.lib.models import User

if TYPE_CHECKING:
	from archinstall.lib.installer import Installer


class LxqtProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('Lxqt', ProfileType.DesktopEnv, description='')

	# NOTE: SDDM is the only officially supported greeter for LXQt, so unlike other DEs, lightdm is not used here.
	# LXQt works with lightdm, but since this is not supported, we will not default to this.
	# https://github.com/lxqt/lxqt/issues/795
	@property
	@override
	def packages(self) -> list[str]:
		return [
			"lxqt",
			"breeze-icons",
			"oxygen-icons",
			"xdg-utils",
			"ttf-freefont",
			"leafpad",
			"slock"
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
			'arandr',
			'arcoinstall-system-config-git',
			'archlinux-logout-git',
			'archlinux-tweak-tool-git',
			'arcolinux-lxqt-git',
			'arcolinux-powermenu-git',
			'arconet-xfce',
			'dmenu',
			'file-roller',
			'ksuperkey',
			'lxappearance',
			'lxqt-arc-dark-theme-git',
			'obconf',
			'pavucontrol',
			'picom-git',
			'polkit-gnome',
			'pavucontrol-qt',
			'thunar',
			'thunar-archive-plugin',
			'thunar-volman',
			'xfce4-notifyd',
			'xfce4-power-manager',
			'xfce4-screenshooter',
			'xfce4-taskmanager',
			'xfce4-terminal',
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
