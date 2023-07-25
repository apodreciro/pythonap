import os
import time


source = ['"C:\\Program Files\\texto"']

target_dir = 'C:\\backup'

target = target_dir + os.sep + \
         time.strftime('%d_%m_%Y_%Mmin_%Sseg') + '.zip'


if not os.path.exists(target_dir):
    os.mkdir(target_dir)

zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))

print('Zip command is: ')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:
    print('O Backup deu certo', target)
else:
    print('O Backup deu errado')
