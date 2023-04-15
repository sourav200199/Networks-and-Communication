#include <bits/stdc++.h>
#include <string.h>
using namespace std;

string sender(string data)
{
    int n = data.length();
    int i = 0;
    string ans = ""; char ch;

    while(i<n)
    {
        ch = data.at(i);

        if(ch == '$' || ch == '@'){
            ans += "$";
            ans += ch;
        }
        else ans += ch;

        i++;
    }

    return "$" + ans + "$";
}

string receiver(string data)
{
    int n = data.length();
    int i = 1;
    char ch; string ans;

    while(i < n-1)
    {
        ch = data.at(i);

        if(ch == '$')
        {
            i++;
            ch = data.at(i);
            ans += ch;
        }
        else ans += ch;

        i++;
    }

    return ans;
}

int main()
{
    int n; string data;

    cout<<"Enter no. of test cases: ";
    cin>>n;

    while(n)
    {
        cout<<"Enter the data: ";
        cin>>data;
        cout<<"The data after byte stuffing is: "<<sender(data)<<endl;
        cout<<"The data after byte unstuffing is: "<<receiver(sender(data))<<endl;
        n--;
    }
}