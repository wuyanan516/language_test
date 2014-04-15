import subprocess
import time

def main():
	while 1 :
		subprocess.check_output("E:\\xampp\\php\\php.exe E:\\xampp\\htdocs\\syc\\gfwrite.php")
		time.sleep(1)

if __name__ == "__main__": 
    main()