#include <bits/stdc++.h>
#include <string.h>
using namespace std;

string sender(string s)
{
    string ans = "";char ch;
    int i = 0, count = 0;

    while(i < s.length())
    {
        ch = s.at(i);
        if(ch == '1' && count == 5){
            ans += "01";
            count = 0;
        }
        else if(ch == '1' && count < 5){
            ans += "1";
            count++;
        }
        else{
            ans += ch;
            count = 0;
        }

        i++;
    }

    return "01111110" + ans + "01111110";
}

string receiver(string data)
{
    int i = 8, count = 0;
    int n = data.length();
    string ans = "";
    char ch;

    while(i < n-7)
    {
        ch = data.at(i);
        if(ch == '0' && count == 5)
        {
            ans += "1";
            count = 0;
            i+=2;
        }
        else if(ch == '1' && count < 5)
        {
            ans += "1";
            count++;
        }
        else{
            ans += ch;
            count = 0;
        }

        i++;
    }

    return ans;
}

int main()
{
    int n;string data;
    cout<<"Enter no. of test cases: ";
    cin>>n;

    while(n)
    {
        cout<<"Enter data: ";
        cin>>data;

        cout<<"Data after bit stuffing: "<<sender(data)<<endl;
        cout<<"Data after bit unstuffing: "<<receiver(sender(data))<<endl;
        n--;
    }

    return 0;
}