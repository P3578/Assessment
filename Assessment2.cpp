#include <iostream>
#include <ctime>
#include <fstream>
using namespace std;
int choice,bal=20000,dip,wit;
int pin = 123456789;
int pass;
class Detail
{
    public : 
        Detail() 
        {
            cout << "\n The name of account holders are : Rakesh Kharva";
            cout << "\n the account holders address is  : Mumbi";
            cout << "\n The branch location is          : Andheri";
            cout << "\n Account number                  : 5678";
        }
};
void line ()
{
    string text;
    ifstream Myfile ("lin1.txt");
    while (getline (Myfile,text))
    {
        cout << text << endl;
    }
}
int main()
{
    time_t now;
    time (&now);
    cout << "\n ------------------------------------ WELCOME TO ATM ----------------------------------------"<<endl;
    cout << "\n                          -------------------------------------                         "<<endl;
    cout << "\n                         Current Date : "<< ctime(&now)                             ;
    cout << "\n                          -------------------------------------                         "<<endl;
    cout << endl;
    line ();
    cout << "\n         Press 1 and Than Press Enter to Access Your Account Via PIN Number";
    cout << "\n\n                                       or"; 
    cout << "\n\n         Press 0 and Press Enter to get Help."<<endl;
    cout << "\n enter the choice = ";
    cin >> choice;  
    switch (choice)
    {
        case 1 :
            cout << "\n -----------------------------------ATM Acount Access ---------------------------------------";
            cout << "\n\n Enter Your ACC Pin Access Number! [Only one attempt is allowed]\n";
            cout << "\n --------------------------------------------------------------------------------------------"; 
            cout << "\n ";
            cin >> pass;
                if(pass != pin)
                {
                    cout << "\n -------------------------------------- THANK YOU -------------------------------------------";
                    cout << "\n You had made your attempt which failed!!! No more attempt allowed!! Sorry!!";
                    line ();
                    cout << "\n Press any key to continue . . . ";
                } 
                else
                do { 
                {
                    cout << "\n --------------------------------- ATM Main Menu Screen -------------------------------------";
                    cout << "\n Enter [1] To Deposite Cash";
                    cout << "\n Enter [2] To Withdraw Cash";
                    cout << "\n Enter [3] To Balance Inquiry";
                    cout << "\n Enter [4] To Exit ATM";
                    cout << "\n PLEASE ENTER A SELECTION AND PRESS RETURN KEY : ";
                    cin >> choice;
                    switch (choice)
                    {
                        case 1 :
                        cout << "\n ------------------------------ ATM ACCOUNT DEPOSIT SYSTEM ----------------------------------";
                        {
                            Detail d1;
                            cout << endl;
                            line ();
                            cout << "\n Present available balance : Rs. "<<bal;
                            cout << "\n Enter the Amount to be Deposited Rs. ";
                            cin >> dip;
                            bal = bal + dip;
                            cout << "\n Your new available blanced amount is Rs. "<<bal;
                            cout << "\n Thank You!";
                            cout << "\n Press any key to Return to the main menu";
                            cin.ignore();
                            cin.get();
                        }
                        break;

                        case 2 :
                        cout << "\n --------------------------------- ATM ACCOUNT withdrawal -----------------------------------";
                        {
                            Detail d2;
                            cout << endl;
                            line ();
                            cout << "\n Enter the Amount to be Withdraw Rs. ";
                            cin >> wit;
                            if (wit > bal)
                            {
                                cout << "\n Insufficient Available Balance in your account.";
                                cout << "\n Sorry !!"; 
                            }
                            bal = bal - wit;
                            cout << "\n Press any key to continue . . . ";
                            cin.ignore();
                            cin.get();
                        }
                        break;

                        case 3 :
                        cout << "\n --------------------------------- Balance Inquiry -----------------------------------";
                        {
                            Detail d3;
                            cout << "\n Available Balance = "<<bal;
                        }
                        cout << "\n Press Enter to continue...";
                        cin.ignore();
                        cin.get();
                        break;

                        case 4 :
                        goto down;
                    }
                   
                } 
                    } while (choice != 4);     
        break;
        case 0 :
            cout << "\n --------------------------------- ATM ACCOUNT STATUS ---------------------------------------";
            cout << "\n      You must have the correct pin number to access this account.";
            cout<<  "\n   See your bank representative for assistance during bank opening hours.";
            cout<<  "\n                    Thanks for, your choice today!!"<<endl;
            line ();
            cout << "\n Press any key to continue . . . ";
        break;
    }
    down:
    return 0;
}