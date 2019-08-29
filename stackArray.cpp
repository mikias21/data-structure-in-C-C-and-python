/*
	Author: Mikias Berhanu
	Date: Aug 29 2019
	Desc: Simple Stack Implementation using array in C++
*/

//preprocessors
#include<iostream>
#include<conio.h>
#define MAX 5 // define a symbolic constant for the stack size
using namespace std;
// define class
class Stack{
	int stack[MAX];
	int top;
	public:
		Stack(){
			top = -1;
		}
		void push();
		void pop();
		void display();
};

//push function
void Stack::push(){
	int item;
	// check for stack overflow
	if(top == MAX - 1){
		cout<<"----------------"<<endl;
		cout<<"stack Overflow"<<endl;
		cout<<"----------------"<<endl;
		return;
	}
	cout<<"enter the number: ";
	cin>>item;
	top++;
	stack[top] = item;
}

//pop function
void Stack::pop(){
	int item;
	// check for stack undeflow
	if(top == -1){
		cout<<"----------------"<<endl;
		cout<<"stack Underflow"<<endl;
		cout<<"----------------"<<endl;
		return;
	}
	item = stack[top];
	cout<<"----------------"<<endl;
	cout<<item<<" is poped"<<endl;
	cout<<"----------------"<<endl;
	top--;
}

// display function
void Stack::display(){
	// check if the stack is empty
	if(top == -1){
		cout<<"----------------"<<endl;
		cout<<"stack is empty"<<endl;
		cout<<"----------------"<<endl;
		return;
	}
	cout<<"----------------"<<endl;
	for(int i = top ; i >=  0 ; i--)
		cout<<stack[i]<<endl;
	cout<<"----------------"<<endl;
	// cout<<endl;
}

// main function
int main(){
	Stack stack;
	int choice;
	do{
		cout<<"1. push"<<endl;
		cout<<"2. pop"<<endl;
		cout<<"3. display"<<endl;
		cout<<"4. exit"<<endl;
		cin>>choice;
		switch(choice){
			case 1: stack.push();
					break;
			case 2: stack.pop();
					break;
			case 3: stack.display();
					break;
			case 4:	cout<<"terminating....."<<endl;
					exit(0);
			default: cout<<"Incorrect choice"<<endl;
		}
	}while(1);

	return 0;
}
