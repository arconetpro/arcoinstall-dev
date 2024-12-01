from typing import TYPE_CHECKING, override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile

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
            'arcolinux-hblock-git',
            'arcolinux-keyring',
            'arcolinux-mirrorlist-git',
            'arcolinux-nlogout-git',
            'arcolinux-paru-git',
            'arcolinux-powermenu-git',
            'arcolinux-wallpapers-candy-git',
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
            'picom-git',
            'playerctl',
            'polkit-gnome',
            'ripgrep',
            'rofi-lbonn-wayland',
            'sparklines-git',
            'sublime-text-4',
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

    @property
    def default_greeter_type(self) -> GreeterType | None:
        return GreeterType.Lightdm
