1. Move weather_screen.service weather_screen.timer to /etc/systemd/system/
2. Enable service 'sudo systemctl enable weather_screen.timer'
3. Run service at boot 'sudo systemctl start weather_screen.timer'
