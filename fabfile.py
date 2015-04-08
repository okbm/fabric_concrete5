# -*- coding: utf-8 -*-
from fabric.api import *
from fabric.decorators import task
from fabric.contrib import files
from fabric.colors import red, green
from cuisine import run
import cuisine

env.hosts = ['vagrant@192.168.56.101']
#env.port = 2222
env.user = 'vagrant'
env.password = 'vagrant'
env.forward_agent = True

@task
def update_packages():
    puts(green('update packages'))
    sudo("apt-get update")

# 使いそうなツール
@task
def setup_devtools():
    puts(green('Installing Devtools'))
    packages = '''
        vim curl wget build-essential tmux screen zsh make sqlite3 tig tree locate git-core python-software-properties unzip
        '''.split()

    for pkg in packages:
        cuisine.package_ensure(pkg)

# アプリケーション
@task
def setup_packages():
    puts(green('Installing Packages'))

    # apache2
    cuisine.package_ensure('apache2')

    # php
    sudo("add-apt-repository -y ppa:ondrej/php5-5.6")
    sudo("apt-get update")

    packages = '''
        php5 libapache2-mod-php5 php5-mysql php5-curl php5-gd php5-mcrypt php5-xdebug php5-cli
        '''.split()

    for pkg in packages:
        cuisine.package_ensure(pkg)

    # other
    cuisine.package_ensure('mysql-server-5.5')

@task
def setup_concrete5():
    puts(green('setup concrete5'))

    # mysql
    run('mysql -uroot -e "CREATE DATABASE concrete5 DEFAULT CHARACTER SET utf8;"')

    # packages download
    with cd('/var/www/html/'):
        # TODO githubからの直接落としてくればいい感じにかけそう
        sudo('curl -L http://www.concrete5.org/download_file/-/view/74619/ > concrete5.zip')
        sudo('unzip concrete5.zip && rm concrete5.zip && mv concrete5* concrete5')

        sudo('chown -R root:www-data concrete5/application/config/')
        sudo('chown -R root:www-data concrete5/application/files/')
        sudo('chown -R root:www-data concrete5/packages/')
        sudo('chmod 775 concrete5/application/config')
        sudo('chmod 775 concrete5/application/files')
        sudo('chmod 775 concrete5/packages/')

@task
def restart_application():
    puts(green('Restarting application'))
    sudo('/etc/init.d/apache2 restart')

@task
def main():
    update_packages()
    setup_devtools()
    setup_packages()
    setup_concrete5()
    restart_application()

    puts(green('finish script'))
