import shutil
import archinstall

from typing import TYPE_CHECKING, override

from archinstall.default_profiles.profile import GreeterType, ProfileType
from archinstall.default_profiles.xorg import XorgProfile

from archinstall.lib.models.users import User
if TYPE_CHECKING:
	from archinstall.lib.installer import Installer


class AwesomeProfile(XorgProfile):
	def __init__(self) -> None:
		super().__init__('Awesome', ProfileType.WindowMgr, description='')

	@property
	@override
	def packages(self) -> list[str]:
		return super().packages + [
			'awesome',
			'alacritty',
			'xorg-xinit',
			'xorg-xrandr',
			'xterm',
			'feh',
			'slock',
			'terminus-font',
			'gnu-free-fonts',
			'ttf-liberation',
			'xsel',
			] + [
			'a-candy-beauty-icon-theme-git',
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
			'yay-git',
			] + [
			'arandr',
			'arcoinstall-system-config-git',
			'archlinux-logout-git',
			'archlinux-tweak-tool-git',
			'arcolinux-awesome-git',
			'arcolinux-local-xfce4-git',
			'arcolinux-powermenu-git',
			'arcolinux-rofi-git',
			'arcolinux-rofi-themes-git',
			'arcolinux-volumeicon-git',
			'arconet-xfce',
			'dmenu',
			'file-roller',
			'lxappearance',
			'numlockx',
			'pavucontrol',
			'picom-git',
			'polkit-gnome',
			'rofi-lbonn-wayland',
			'thunar',
			'thunar-archive-plugin',
			'thunar-volman',
			'vicious',
			'volumeicon',
			'xfce4-notifyd',
			'xfce4-power-manager',
			'xfce4-screenshooter',
			'xfce4-terminal',
		] + [
			'arcolinux-sddm-simplicity-git',
		]

	@override
	def install(self, install_session: 'Installer') -> None:
		super().install(install_session)

		# TODO: Copy a full configuration to ~/.config/awesome/rc.lua instead.
		with open(f"{install_session.target}/etc/xdg/awesome/rc.lua") as fh:
			awesome_lua = fh.read()

		# Replace xterm with alacritty for a smoother experience.
		awesome_lua = awesome_lua.replace('"xterm"', '"alacritty"')

		with open(f"{install_session.target}/etc/xdg/awesome/rc.lua", 'w') as fh:
			fh.write(awesome_lua)

		# TODO: Configure the right-click-menu to contain the above packages that were installed. (as a user config)

		# TODO: check if we selected a greeter,
		# but for now, awesome is intended to run without one.
		with open(f"{install_session.target}/etc/X11/xinit/xinitrc") as xinitrc:
			xinitrc_data = xinitrc.read()

		for line in xinitrc_data.split('\n'):
			if "twm &" in line:
				xinitrc_data = xinitrc_data.replace(line, f"# {line}")
			if "xclock" in line:
				xinitrc_data = xinitrc_data.replace(line, f"# {line}")
			if "xterm" in line:
				xinitrc_data = xinitrc_data.replace(line, f"# {line}")

		xinitrc_data += '\n'
		xinitrc_data += 'exec awesome\n'

		with open(f"{install_session.target}/etc/X11/xinit/xinitrc", 'w') as xinitrc:
			xinitrc.write(xinitrc_data)

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
