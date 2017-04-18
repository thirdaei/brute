def kali_build():

    print O + "Updating Repositories..." + W
    sleep(1.5)
    os.system("sudo apt-get update")
    print O + "Installing essential packages..." + W
    sleep(1.5)
    os.system("sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-setuptools")
    os.system("sudo apt-get install python-selenium")
    os.system("sudo apt-get install firefoxdriver")
    print O + "Installing pip modules" + W
    sleep(1.5)
    os.system("sudo pip install -r requirements.txt")
    print G + "Done installing dependences!" + W
    sys.exit(0)

def ubuntu_build():
    print O + "Updating Repositories..." + W
    sleep(1.5)
    os.system("sudo add-apt-repository universe")
    os.system("sudo apt-get update")
    print O + "Installing essential packages..." + W
    sleep(1.5)
    os.system("sudo apt-get install build-essential libssl-dev libffi-dev python-dev python-setuptools")
    os.system("sudo apt-get install python-pip") # result of universe repo
    print O + "Installing pip modules" + W
    sleep(1.5)
    os.system("sudo pip install -r requirements.txt")
    os.system("sudo pip install -U selenium")


# OS X / Darwin
def osx_build():
    print O + "Installing Homebrew..." + W
    sleep(1.5)
    os.system("""/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)" """)
    os.system("brew install Caskroom/cask/firefox")
    os.system("sudo easy_install pip")
    print O + "Installing pip modules" + W
    sleep(1.5)
    os.system("sudo easy_install selenium")
    # If Crytography returns errorS
    os.system("brew install libffi")
    os.system("sudo pip install -r requirements.txt")
    print O + "Getting GeckoDriver" + W
    os.system("cd deps && sudo tar -xvf geckodriver-v0.14.0-linux32.tar.gz && sudo mv -R geckodriver $HOME")
    print G + "[!] Done installing dependences! [!]" + W
    sys.exit(0)

while True:
    print ""
    print "(1) Kali Linux x32/x64"
    print "(2) Ubuntu / Parrot OS"
    print "(3) Mac OS X / Darwin"
    print ""
    getos = raw_input(">> ")
    if getos == "1":
        kali_build()
        break
    elif getos == "2":
        ubuntu_build()
        print O + "Getting GeckoDriver" + W
        sleep(1.5)
        os.system("cd deps && sudo tar -xvf geckodriver-v0.13.0-linux32.tar.gz && sudo mv geckodriver /usr/bin ")
        print G + "Done installing dependences!" + W
        break
    elif getos == "3":
        osx_build()
    #elif getos == "4":
    #    osx_build()
    else:
        continue