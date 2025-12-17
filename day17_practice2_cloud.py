from datetime import datetime

with open('deploy_log.txt', 'a') as file:
    file.write(f'Deployment run at {datetime.now()}\n')