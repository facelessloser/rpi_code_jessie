1. Move templogger.service templogger.timer to /etc/systemd/system/

2. Enable service 'sudo systemctl enable templogger.timer'
3. Run service at boot 'sudo systemctl start templogger.timer'
