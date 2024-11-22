# Name, Language
project('slstatus','cpp')
version='1.1'
# Files
src=['slstatus.cpp','util.cpp']
components=[
  'components/kernel_release.cpp',
  'components/load_avg.cpp',
  'components/swap.cpp',
  'components/keymap.cpp',
  'components/battery.cpp',
  'components/user.cpp',
  'components/num_files.cpp',
  'components/ram.cpp',
  'components/volume.cpp',
  'components/cpu.cpp',
  'components/run_command.cpp',
  'components/uptime.cpp',
  'components/keyboard_indicators.cpp',
  'components/cat.cpp',
  'components/datetime.cpp',
  'components/ip.cpp',
  'components/netspeeds.cpp',
  'components/wifi.cpp',
  'components/entropy.cpp',
  'components/hostname.cpp',
  'components/temperature.cpp',
  'components/disk.cpp'
]
# Dependencies (x11, xfreetype)
x11_dep = [dependency('x11'),dependency('freetype2'),dependency('xft'),dependency('fontconfig')]
#others (ugly ahh hell ik ik), Wno-d-d is in the OG Makefile
add_project_arguments(['-DVERSION="'+version+'"','-Wno-deprecated-declarations'],language : 'cpp')

install='/usr/local/bin/'

executable('slstatus',
            src,
            components,
            dependencies : x11_dep,
            install : true,
            install_dir : install)
install_man('slstatus.1')

