#. TDA_token_generator for TD Ameritrade (TOS)

#. Need a TD Ameritrade Account

#. Need a TD Ameritrade developer account on https://developer.tdameritrade.com/

   Go to My Apps from your TD Ameritrade developer accounts
   and create a new apps by clicking >>Add a new App<<
   
   Then in >>App Name<< field: Anything (give any name)

   In >>Callback URL<< field: https://localhost

   In >>What is the purpose of your application?<< : Anything (write your purpose)

   click >>Create App<<
   
   After creating app click your app name. You will find a >>Consumer Key<<. Copy this key.

#. Need to install Python >=3.6

#. Need to install tda-api

#. Run tda_token_generator.py and follow the instructions

#. The generated TDA_Auth_Token.json file is valid for 85 days. If the token file is not valid anymore
   delete the TDA_Auth_Token.json file and run tda_token_generator.py again

#. Note: Nuitka is only used for compilation to a binary (if needed for distribution).
