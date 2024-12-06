from typing import override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile


class PlasmaProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('KDE Plasma', ProfileType.DesktopEnv, description='')

	@property
	@override
	def packages(self) -> list[str]:
		return [
			"plasma-meta",
			"konsole",
			"kate",
			"dolphin",
			"ark",
			"plasma-workspace"
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
			'neofetch',
			'noto-fonts',
			'paru-git',
			'ttf-hack',
			'variety',
			'yay-git',
			] + [
			'archlinux-logout-git',
			'archlinux-tweak-tool-git',
			'arcolinux-arc-kde',
			'arcolinux-plasma-keybindings-git',
			'arcolinux-plasma-servicemenus-git',
			'arcolinux-plasma-theme-candy-beauty-arc-dark-git',
			'arcolinux-plasma-theme-candy-beauty-nordic-git',
			'arcolinux-plasma-theme-surfn-arc-dark-git',
			'arcolinux-plasma-theme-surfn-nordic-git',
			'ark',
			'breeze',
			'dolphin-plugins',
			'gwenview',
			'kde-gtk-config',
			'polkit-gnome',
			'rofi-lbonn-wayland',
			'surfn-plasma-dark-icons-git',
			'surfn-plasma-light-icons-git',
			'volumeicon',
			'xfce4-terminal',
			'yakuake',
		]

	@property
	@override
	def default_greeter_type(self) -> GreeterType | None:
		return GreeterType.Sddm
