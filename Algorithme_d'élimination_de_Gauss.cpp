#include<iostream>
#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cout<<"enter matrix dimension :";
    cin>>n;
    float  A[n+1][n+1];
    float b[n+1];
    cout<<"enter the value of matrix A : "<<endl;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cin>>A[i][j];
        }
    }
    cout<<endl;
    cout<<"enter the values of second member b : ";
    for(int i=1;i<=n;i++)
    {
        cin>>b[i];
    }
    for(int k=1;k<n;k++)
    {
        if(A[k][k]==0)
        {
            cout<<"the pivot is zero so swapping row k with row r > k is writing the matrix";
            return 0;
        }

        
        for(int i=k+1;i<=n;i++)
        {
            float c;
            c = A[i][k]/A[k][k];
            b[i] = b[i] - c*b[k];
            A[i][k] = 0;
            for(int j=k+1;j<=n;j++)
            {
                 A[i][j] = A[i][j] - c*A[k][j];
            }
        }
        
    }
    if(A[n][n] == 0)
    {
        cout<<"error : the pivot is zero ";
        return 0;
    }
    cout<<"the matrix after  the Gaussian elimination method"<<endl;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=n;j++)
        {
            cout<<A[i][j]<<" ";
        }
        cout<<endl;
    }
cout<<"b after  the Gaussian elimination method"<<endl;
    for(int i=1;i<=n;i++)
    {
    	cout<<b[i]<<" ";
    }
    cout<<endl;
    float X[n+1]={0};
    X[n] = b[n]/A[n][n];
    int i = n-1;
    while(i>=1)
    {
        float s ;
        s=b[i];
        int j;
        j = i+1;
        while(j<=n)
        {
            s = s - A[i][j]*X[j];
            j++;
        }
        X[i] = s/A[i][i];
        i--;
    }
    cout<<"The solutions of your system : "<<endl;
    for(int i=n;i>0;i--)
    {
        cout<<"x"<<i<<" : "<<X[i]<<endl;
    }







}
