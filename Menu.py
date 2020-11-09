import os
import getpass
import subprocess
import pyttsx3
while(True):
    def hadoopmainMenu():
        os.system("clear")
        os.system('tput setaf 7')
        print("================================================================================")
        print("\t\t\tWELCOME TO THE HADOOP MENU (^-^) !!")
        print("================================================================================")
        while True:
            os.system('tput setaf 3')
            print("""
                        Enter 1 TO INSTALL HADOOP
                        Enter 2 TO CONFIGURE DATA NODE/ NAME NODE
                        Enter 3 TO FORMAT NAME NODE
                        Enter 4 TO START HADOOP SERVICE
                        Enter 5 TO STOP HADOOP SERVICE
                        Enter 6 TO GET CLUSTER REPORT
                        Enter 7 TO SEE THE FILES
                        Enter 8 TO RETURN TO THE MAIN MENU
                    """)
            choice = input("Enter your choice: ")
            if choice == "1":
                os.system("rpm -ihv  jdk-8u171-linux-x64.rpm")
                os.system("rpm -ihv hadoop-1.2.1-1.x86_64.rpm --force")
            elif choice == "2":
                os.system("vim /etc/hadoop/hdfs-site.xml")
                os.system("vim /etc/hadoop/core-site.xml")
            elif choice == '3':
                os.system("hadoop namenode -format")
            elif choice == "4":
                service = input("""
                                    ENTER 1: FOR NAMENODE
                                    ENTER 2: FOR DATANODE
                                        """)
                if service == "1":
                    os.system("hadoop-daemon.sh start namenode")
                elif service == "2":
                    os.system("hadoop-daemon.sh start datanode")
                else:
                    print("wrong choice!!! :( ")
                    return
            elif choice == 5:
                service1 = input("""
                                    ENTER 1: FOR NAMENODE
                                    ENTER 2: FOR DATANODE
                                        """)
                if service1 == "1":
                    os.system("hadoop-daemon.sh stop namenode")
                elif service1 == "2":
                    os.system("hadoop-daemon.sh stop datanode")
                else:
                    print("wrong choice!!! :( ")
                    return
            elif choice == "6":
                os.system("hadoop dfsasdmin -report")
            elif choice == "7":
                os.system("hadoop fs -ls /")
            else:
                input("Press Enter to continue.....")
                return
            os.system('clear')
    ##################################################################

                
    def aws():	
        os.system('clear')
        os.system('tput setaf 7')
        print("===========================================================================") 
        print("\t\t WELCOME TO AWS MENU DRIVEN PROGRAM !!! :D ") 
        print("===========================================================================")
        os.system("aws configure")
        while(True):
            def key():
                while True:
                    os.system('tput setaf 7')
                    print("===========================================================================")
                    print("\t\t AWS KEY  MENU !!! :D ")
                    print("===========================================================================")
                    os.system('tput setaf 6')
                    print("""
                                Enter 1: TO CREATE KEY
                                Enter 2: TO DELETE KEY
                                Enter 3: TO DESCRIBE KEY PAIR
                                Enter 4: TO EXIT
                            """)
                    choice = input(" Enter your choice : ")
                    if choice == "1":
                        key_name = input("Enter Key-name: ")
                        os.system("aws ec2 create-key-pair --key-name {} --query KeyMaterial --output text >  {}".format(key_name,key_name))
                    elif choice == "2":
                        key_name = input("Enter Key-name")
                        os.system("aws ec2 delete-key-pair --key-name {}".format(key_name))
                    elif choice == "3":
                        os.system("aws ec2 describe-key-pairs")
                    else:
                        print("Wrong Choice")
                        return
            def securityGroup():
                while(True):
                    os.system('tput setaf 7')
                    print("===========================================================================")
                    print("\t\tWELCOME TO SECURITY GROUP MENU !!! :D ")
                    print("===========================================================================")
                    os.system('tput setaf 6')

                    print("""
                            Enter 1: TO CREATE SECURITY GROUP
                            Enter 2: TO DESCRIBE SECURITY GROUP
                            Enter 3: TO DELETE SECURITY GROUP
                            Enter 4: TO ADD RULE OF SECURITY GROUP
                            Enter 5: TO DELETE RULE OF SECURITY GROUP
                            Enter 6: TO EXIT
                        """)
                    choice = int(input("Enter your choice:"))
                    if choice == 1:
                        description = input("Enter Description of sg : ")
                        Group_name = input("Enter sg group Name : ")
                        os.system("aws ec2  create-security-group --description {} --group-name {}".format(description,Group_name))
                    elif choice == 2:
                        os.system("aws ec2 describe-security-groups")
                    elif choice == 3:
                        id1 = input("Enter sg Id: ")
                        os.system(" aws ec2 delete-security-group --group-id {}".format(id1))
                    elif choice == 4:
                        print("     Enter 1 for ingress \n Enter 2 for egress")
                        add = input("Enter your choice : ")
                        security_id = input("Enter security id: ")
                        protocol = input("Enter protocol: ")
                        port = input("Enter Port: ")
                        cidr = input("Enter Cidr: ")
                        if add == "1":
                            os.system("aws ec2 authorize-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(security_id,protocol,port,cidr))
                        elif add == "2":
                            os.system("aws ec2 authorize-security-group-egress --group-id {} --protocol {} --port {} --cidr {}".format(security_id, protocol, port, cidr))
                        else:
                            print()
                    elif choice == 5:
                        print("Enter 1 for ingress \nEnter 2 for egress")
                        delete = input("Enter your choice : ")
                        security_id = input("            Enter security id: ")
                        protocol = input("          Enter protocol: ")
                        port = input("          Enter Port: ")
                        cidr = input("          Enter Cidr: ")
                        if delete == "1":
                            os.system("aws ec2 revoke-security-group-ingress --group-id {} --protocol {} --port {} --cidr {}".format(security_id,protocol,port,cidr))
                        elif delete == "2":
                            os.system("aws ec2 revoke-security-group-egress --group-id {} --protocol {} --port {} --cidr {}".format(security_id, protocol, port, cidr))
                        else:
                            print("Wrong Choice")
                    else:
                        os.system('clear')
                        return
                        
                        
            def volume():
                while(True):
                    os.system('tput setaf 7')
                    print("===========================================================================")
                    print("\t\t\tAWS VOLUME MENU  :D ")
                    print("===========================================================================")
                    os.system('tput setaf 4')

                    print("""
                            Enter 1 TO DESCRIBE VOLUME
                            Enter 2 TO CREATE VOLUME
                            Enter 3 TO DELETE VOLUME
                            Enter 4 TO ATTACH VOLUME
                            Enter 5 TO DETACH VOLUME
                            Enter 6 TO RETURN TO MAIN MENU
                        """)
                    choice=input("Enter your Choice: ") 
                    if choice == "1":
                        os.system("aws ec2 describe-volumes")
                    elif choice == "2":
                        az = input("Enter AZ : ")
                        size = input("size: ")
                        os.system("aws ec2 create-volume --availability-zone {} --size {}".format(az,size))
                    elif choice == "3":
                        volume_id = input("Enter Volume ID : ")
                        os.system("aws ec2 delete-volume --volume-id {}".format(volume_id))
                    elif choice == "4":
                        device = input("Enter  device Name: ")
                        instance_id = input("Instance ID: ")
                        volume_id = input("Volume ID: ")
                        os.system("aws ec2 attach-volume --device {} --instance-id {} --volume-id {} ".format(device,instance_id,volume_id))
                    elif choice == "5":
                        volume_id = input("Volume ID: ")
                        os.system("aws ec2 detach-volume --volume-id {} ".format(volume_id))
                    else:
                        return
            def ec2():
                while(True):
                    os.system('tput setaf 7')
                    print("================================================================================")
                    print("\t\t\t\tWELCOME TO EC-2 SERVICE !!")
                    print("================================================================================")
                    os.system('tput setaf 4')
                    print("""
                            Enter 1:TO GET INFORMATION ABOUT YOUR INSTANCES
                            Enter 2:TO LAUNCH AN INSTANCE
                            Enter 3:TO START AN INSTANCE
                            Enter 4:To STOP AN INSTANCE
                            Enter 5:TO RETURN TO MAIN MENU
                            Enter 6:TO EXIT
                            """)
                    e = input("Enter your choice: ")
                    if e == "1":
                        os.system("aws ec2 describe-instances")
                    elif e == "2":
                        cnt=int(input("How many instance you want to launch:"))
                        key_name = input("Enter your keyname:")
                        os.system("aws ec2 run-instances  --image-id ami-0e306788ff2473ccb --instance-type t2.micro --count {} --subnet-id subnet-a6cac3ce --key-name {} ".format(cnt,key_name))
                        print("Instance Launched !!!")
                    elif e == "3":
                        id2 = input("Enter your instance id :")
                        os.system("aws ec2 start-instances --instance-ids {}".format(id2))
                    elif e == "4":
                        id3 = input("Enter your instance id :")
                        os.system("aws ec2 stop-instances --instance-ids {}".format(id3))
                    elif e == "5":
                        return
                    else:
                        os.system('tput setaf 7')
                        exit()
            def s3():
                while(True):
                    os.system("clear")
                    os.system('tput setaf 7')
                    print("================================================================================")
                    print("\t\t\t\tWELCOME TO S3 SERVICE !!")
                    print("================================================================================")
                    os.system('tput setaf 4')
                    print('''
                            Press 1: FOR CREATING BUCKET
                            Press 2: FOR ADDING OBJECT
                            Press 3: FOR BUCKET LIST
                            Press 4: FOR DELETING BUCKET
                            Press 5: FOR DELETING OBJECT OF BUCKET
                        ''')
                    s=input("Enter your choice :")
                    if s == "1":
                        bn=input("ENTER BUCKET NAME: ")
                        r=input("ENTER REGION: ")
                        os.system(" aws s3api create-bucket --bucket {bucket}  --region {region} --create-bucket-configuration  LocationConstraint=ap-south-1".format(bucket=bn,region=r))
                    elif s == "2":
                        bn=input("\n ENTER BUCKET NAME: ")
                        print("LIST OF OBJECTS PRESENT IN {bucket}".format(bucket=bn))
                        os.system("aws s3 ls s3://{bucket} ".format(bucket=bn))
                        op=input("ADD AN OBJECT (Y/N):")
                        if op == "Y":
                            lc=input("ENTER location: ")
                            os.system("aws s3 ls s3://{bucket} ")
                            os.system("aws s3 sync {location} s3://{bucket} --acl public-read".format(location=lc,bucket=bn))
                    elif s == "3":
                        os.system('aws s3api list-buckets --query "Buckets[].Name"')
                    elif s == "4":
                        bn=input("\n ENTER BUCKET NAME: ")
                        r=input("\n ENTER REGION:")
                        os.system("aws s3api delete-bucket --bucket {bucket} --region {region}".format(bucket=bn,region=r))
                    elif s == "5":
                        bn=input("\n ENTER BUCKET NAME: ")
                        on=input("\n ENTER OBJECT NAME: ")
                        os.system("aws s3 rm s3://{bucket}/{oname}".format(bucket=bn,oname=on))
                    else:
                        return
                        
            def cloudFront():
                while(True):
                    os.system("clear")
                    os.system('tput setaf 7')
                    print("================================================================================")
                    print("\t\t\t\tWELCOME TO EC-2 SERVICE !!")
                    print("================================================================================")
                    os.system('tput setaf 4')
                    cf = input('Press 1: for creating distribution')
                    if cf == "1":
                        bucketnm=input("\n ENTER RESPECTIVE BUCKET NAME:")
                        objectnm=input("\n ENTER THE OBJECT NAME YOU WANT TO DISTRIBUTE:")
                        os.system("aws cloudfront create-distribution --origin-domain-name {}.s3.amazonaws.com --default-root-object {}".format(bucketnm,objectnm))
                    else:
                        print("Exit")
                        return
            os.system('clear')
            os.system('tput setaf 7')
            print("===========================================================================")
            print("\t\t AWS MENU !!! :D ")
            print("===========================================================================")
            os.system('tput setaf 6')
            print("""
                    Press 1: FOR CREATE KEY PAIR
                    Press 2: FOR SECURITY GROUP	
                    Press 3: FOR EC2 INSTANCES
                    Press 4: FOR VOLUMES
                    Press 5: FOR S3
                    Press 6: FOR CLOUD FRONT
                    Press 7: TO RETURN TO MAIN MENU
                """)
            c = int(input("\n Enter Your Choice:"))
            if c == 1:
                key()
            elif c == 2:
                securityGroup()
            elif c == 3:
                ec2()
            elif c == 4:
                volume()
            elif c == 5:
                s3()
            elif c == 6:
                cloudFront()
            else:
                return
    ###############################################################################################################


    def Lvm():
        while True:
            os.system('clear')
            os.system('tput setaf 7')
            print("===========================================================================")
            print("\t\t LOGICAL VOLUME MANAGEMENT !!! :D ")
            print("===========================================================================")
            os.system('tput setaf 2')
            print("WELCOME TO MY MENU")
            print("PRESS 1:DISPLAY HARDISK INFORMATION")
            print("PRESS 2:CREATE PV,CREATE VG,CREATE LV,CREATE FOLDER,MOUNT LV")
            print("PRESS 3:DISPLAY LV")
            print("PRESS 4:EXTEND LV")
            print("PRESS 5:REDUCE LV")
            print("PRESS 6:FOR RETURNING TO MAIN MENU")
            z = input("ENTER YOUR CHOICE:")
            if int(z) == 1:
                os.system("fdisk -l")
            elif int(z) == 2:
                a = str(input("ENTER 1ST DISK NAME:"))
                b = str(input("ENTER 2ND DISK NAME:"))
                
                os.system("pvcreate /dev/"+a)
                os.system("pvcreate /dev/"+b)
                
                c = str(input("ENTER VG NAME:"))
                os.system("vgcreate "+c+" /dev/"+a+" /dev/"+b)
                
                d = str(input("ENTER NAME OF LV:"))
                e = str(input("ENTER SIZE OF LV:"))
                
                os.system("lvcreate --size +"+e+"G --name "+d+" "+c)
                
                os.system("mkfs.ext4 /dev/"+c+"/"+d)

                f = str(input("ENTER FOLDER NAME:"))
                os.system("mkdir /"+f)
                
                os.system("mount /dev/"+c+"/"+d+" "+"/"+f)
            elif int(z) == 3:
                os.system("lvdisplay "+c+"/"+d)
            elif int(z) == 4:
                g = str(input("ENTER SIZE TO BE INCREASED:"))
                os.system("lvextend --size +"+g+"G  /dev/"+c+"/"+d)
                os.system("resize2fs /dev/"+c+"/"+d)
            elif int(z) == 5:
                h = str(input("ENTER SIZE UPTO WHICH LV SHOULD BE REDUCED:"))
                os.system("lvreduce -r -L"+h+"G /dev/"+c+"/"+d)
            
        else:
            return
    ################################################################################################################
    def docker():
        while True:
            os.system('clear')
            os.system('tput setaf 7')
            print("===========================================================================")
            print("\t\t AWS MENU !!! :D ")
            print("===========================================================================")
            os.system('tput setaf 8')

            print("WELCOME TO MY DOCKER MENU")
            print("PRESS 1:TO START YOUR DOCKER SERVICE")
            print("PRESS 2:TO PULL IMAGE YOU WANT")
            print("PRESS 3:TO GET DOCKER INFORMATION")
            print("PRESS 4:DOCKER RUN")
            print("PRESS 5:DOCKER START")
            print("PRESS 6:DOCKER STOP")
            print("PRESS 7:TO DELETE DOCKER OS")
            print("PRESS 8:TO DELETE DOCKER OS IMAGE")
            print("PRESS 9:To RETURN TO MAIN MENU")
            z = input("ENTER YOUR CHOICE:")
            if int(z) == 1:
                os.system("systemctl start docker")
            elif int(z) == 2:
                a = str(input("which os image to pull:"))
                b = str(input("version:"))
                os.system("docker pull "+a+":"+b)
            elif int(z) == 3:
                os.system("docker ps -a")
            elif int(z) == 4:
                c = str(input("Name for docker os:"))
                d = str(input("Which docker image to be used:"))
                e = str(input("version:"))
                os.system("docker run -it --name "+c+" "+a+":"+b)
            elif int(z) == 5:
                f = str(input("Name/id of docker os:"))
                os.system("docker start "+f)
            elif int(z) == 6:
                g = str(input("Name/id of docker os:"))
                os.system("docker stop "+g)
            elif int(z) == 7:
                h = str(input("Name/id of docker os:"))
                os.system("docker rm "+h)
            elif int(z) == 8:
                i = str(input("Enter image you want to remove:"))
                os.system("docker rmi -f "+i)
            elif int(z) == 9:
                os.system("exit()")
        else:
            return

    ########################################################################

    def linuxbasic():
        while(True):
            os.system('clear')
            os.system('tput setaf 7')
            print("===========================================================================")
            print("\t\t WELCOME TO LINUX AUTOMATION TOOL  !!! :D ")
            print("===========================================================================")
            os.system('tput setaf 3')

            print('''
		    Press 1 : To View RHEL version information
		    Press 2 : To check pwd the working directory
		    Press 3 : To create a new files
		    Press 4 : To check a files are created or removed
		    Press 5 : To changes directory
		    Press 6 : To removes files 
		    Press 7 : To makes directories
		    Press 8 : To check lists the current running processes
		    Press 9 : To check lists directory contents
		    Press 10 : To Install software
		    Press 11 : To Reboot system	
		
		

	''')
            ch = input("Enter your choice : ")
	

            if int(ch) == 1:
                os.system(" /etc/redhat-release")
            elif int(ch) == 2:
                os.system("pwd")
            elif int(ch) == 3:
                filename = input("Enter File name do want to create: ")
                os.system("touch {}".format(filename))
            elif int(ch) == 4:
                os.system("ls")
            elif int(ch) == 5:
                os.system("cd")
            elif int(ch) == 6:
                fname = input("Enter the name of file you want to remove: ")
                os.system("rm {}".format(fname))
            elif int(ch) == 7:
                dirname = input("Enter the name of directory you want to create: ")
                os.system("mkdir {}".format(dirname))
            elif int(ch) == 8:
                os.system("ps -ef")
            elif int(ch) == 9:
                os.system("ls /etc")
            elif int(ch) == 10:
                sname = input("Enter software name you want to install: ")
                os.system("yum install {}".format(sname))
            elif int(ch) == 11:
                os.system("systemctl reboot")
            else:
                return

    ########################################################################            
    os.system("clear")
    os.system('tput setaf 7')
    print("================================================================================")
    print("\t\t\t\tWELCOME TO THE MENU !!")
    print("================================================================================")
    os.system('tput setaf 6')
    print("""
                Press 1: For HADOOP
                Press 2: For AWS	
                Press 3: For LOGICAL VOLUME MANAGEMENT
                Press 4: For DOCKER
                Press 5: For BASIC LINUX COMMANDS
                Press 6: For EXIT
             """)
    os.system('tput setaf 7')
    c = int(input("\n Enter Your Choice:"))
    if c == 1:
        hadoopmainMenu()
    elif c == 2:
        aws()
    elif c == 3:
        Lvm()
    elif c == 4:
        docker()
    elif c == 5:
        linuxbasic()
    else:
        exit()









