#include<iostream>
using namespace std;

int Fibonacci(int num);

int main(){
	for(int i=1;i<=200;i++){
		cout<<"Fibonacci.of("<<i<<") == "<<Fibonacci(i)<<endl;
	}
	
	return 0;
}


int Fibonacci(int num){
	if(num == 1 || num == 2)
		return 1;
	return Fibonacci(num-1) + Fibonacci(num-2);
}

