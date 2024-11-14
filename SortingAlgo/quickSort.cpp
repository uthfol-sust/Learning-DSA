#include<bits/stdc++.h>
using namespace std;

int partion(vector<int> &arr, int l, int h)
{
    int pivot = arr[l];
    int i=l, j= h;

    while(i<j){
        
        while (i <= h && arr[i]<=pivot){
            i++;
        }
        
        while (j >= l && arr[j]>pivot){
            j--;
        }

        if(i<j){
            swap(arr[i],arr[j]);
        }
    }

    swap(arr[l],arr[j]);

    return j;
}

void QuickSort(vector<int>&arr, int l, int h)
{
    if(l<h){
        int mid = partion(arr,l,h);
        QuickSort(arr,l,mid-1);
        QuickSort(arr,mid+1,h);
    }
}

int main(){
    vector<int> arr = {10,20,13,2,5,13,16,77,20,34,21};

    int n = arr.size();

    QuickSort(arr,0,n-1);
    
    cout << "Sorted Array : ";
    for(auto it:arr){
        cout << it << " ";
    }
    
    return 0;
}
