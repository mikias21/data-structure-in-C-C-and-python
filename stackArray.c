/*
	Author: Mikias Berhanu
	Date : Aug 29 2019
	Desc: Simple Stack Implementation in C using struct and array
*/

//include preprocessors
#include<stdio.h>
#include<stdlib.h>
#include<conio.h>
#define MAX 5 // define symbolic constant for the stack array

// creat a struct data stracture for the stack we are create
struct stack{
	int top;   
	int stack[MAX];
};

//create typedef pointer for the stack
typedef struct stack stack;

//push function
void push(){
	stack *ptr;
	int item;
	// check if the stack is full
	if(ptr->top == MAX - 1){
		printf("stack Overflow\n");
		return;
	}
	printf("enter the number : ");
	scanf("%d",&item);
	ptr->stack[ptr->top] = item;
	ptr->top++;
}

//pop function
void pop(){
	int item;
	stack *ptr;
	// check if the stack is empty
	if(ptr->top == -1){
		printf("stack Underflow\n");
		return;
	}
	item = ptr->stack[ptr->top];
	printf("%d is poped\n" , item);
}

//display function
void display(){
	int i;
	stack *ptr;
	// check if the stack is empty
	if(ptr->top == -1){
		printf("stack is empty\n");
		return;
	}
	for(i = ptr->top ; i >= 0 ; i++){
		printf("%d -> " , ptr->stack[i]);
	}
}

//main function
int main(){
	stack *ptr;
	ptr->top = -1;
	int choice;
	do{
		printf("1. push\n");
		printf("2. pop\n");
		printf("3. display\n");
		printf("4. exit\n");
		scanf("%d",&choice);
		switch(choice){
			case 1: push();
					break;
			case 2: pop();
					break;
			case 3: display();
					break;
			case 4: exit(0);
			default: printf("incorrect choice\n");
		}
	}while(1);
	return 0;
}
