# python-pirates-project-cohort-1

DEVELOPER "GETTING STARTED" INSTRUCTIONS 

    SUMMARY

    This app was created with the goal to provide an interactive environment for users to access up-to-date data on stocks of their interests.
	

    ENVIRONEMT SETUP
	
    1. Create a virtural inveirnemnt
	
        Method 1: with conda installed, at command prompt, run ' conda create -n myenv python=3.8 '      # python3.8 was the version used to create this app
		
		Method 2: at command prompt, run   '  python3 -m venv myenv '
		
		
	2. Activate virtural inveirnemnt
	
		Method 1: with conda installed, at command prompt, run ' conda activate myenv '      
		
		Method 2:  on Windows, run:   ' myenv\Scripts\activate.bat '
						 on Unix or MacOS, run: source myenv/bin/activate
						 
						 
	3. Install requiremnets for te app: run pip3 install -r requirements.txt
	
	
	APP FUNCTIONALITY SUMMARY
	
	1. Annonomous users are presented with Home, Login and Signup options on the menu bar
	
	2. If a new user attempted to login, they will be directed to the signup page
	
	3. After signup, the user is directed to login page to login.  Any existing user can go diretly to the login page

	4. After login, the user has options for Home, Dashboard, Update and Logout pages
	
	5. On the Dashboard page, the user is presented with the curent information on stocks they selected.  The user has options to add and delete stocks (tickers) 
	
	6. On the Update page, the user can change username, password, email and enter stocks symbols.   The form is preloaded with username, email and any stocks in the account.
	These inforamtion was preloaded with the assumption that they typically don't change.  But if user enters new inforamtion, it will be saved.
	
	7. The user stay login as log as the logout option is not chosen.   