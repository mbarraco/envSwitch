#!/usr/bin/env python
# Unity indicator for evolution-less clock and date display
# author: phil ayres
# 24 Oct 2011
 
import gtk
import appindicator
import os, sys, fileinput, subprocess

class EnvironmentSwitch:
    FILE = '/home/marianobarraco/Platform/web/app_dev.php'
    ENVIRONMENT = 'DEV';

    DEV_SETTING_LINE = "'dev', true"
    PROD_SETTING_LINE = "'prod', false"
    CONSOLE_STUFF = 'cd; cd Platform; app/console assets:install /var/www/Platform/web/vdevelopment; app/console assetic:dump --env=prod'
    CONSOLE_STUFF = 'cd'

    def __init__(self):
    	self.ind = appindicator.Indicator("switch-indicator",
                                         "",
                                         appindicator.CATEGORY_APPLICATION_STATUS)
        self.ind.set_status(appindicator.STATUS_ACTIVE)
        self.ind.set_attention_icon("switch-env")
        self.menu_setup()
        self.ind.set_menu(self.menu)

    def menu_setup(self):
    	self.menu = gtk.Menu()

        self.switch_item = gtk.MenuItem("Switch ")
        self.switch_item.connect("activate", self.switch)
        self.switch_item.show()
        self.menu.append(self.switch_item)

        self.quit_item = gtk.MenuItem("Quit")
        self.quit_item.connect("activate", self.quit)
        self.quit_item.show()
        self.menu.append(self.quit_item)

    def switch(self, widget):
        if self.ENVIRONMENT == 'DEV':
            self.ENVIRONMENT = 'PROD'
            self.switchEnvInFile(self.DEV_SETTING_LINE, self.PROD_SETTING_LINE)
            # self.runConsoleStuff();
        else:
            self.ENVIRONMENT = 'DEV'
            self.switchEnvInFile(self.PROD_SETTING_LINE, self.DEV_SETTING_LINE)

        self.ind.set_label(self.ENVIRONMENT)
        f = open(self.FILE, 'r+')

    def runConsoleStuff(self):
        subprocess.call(self.CONSOLE_STUFF)

    def switchEnvInFile(self, textToSearch, textToReplace):
            s = open(self.FILE).read()
            s = s.replace(textToSearch, textToReplace)
            f = open(self.FILE, 'w')
            f.write(s)
            f.close()

    def start(self, widget):
        self.ind.set_label(self.ENVIRONMENT)
        gtk.main()


    def quit(self, widget):
        sys.exit(0)

if __name__ == "__main__":		

	pomodoro = EnvironmentSwitch()
	pomodoro.start(False)
