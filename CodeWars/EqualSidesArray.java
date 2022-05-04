package com.codewars.katas.collections;

import java.util.Arrays;

public class EqualSidesArray {

	public static void main(String[] args) {
		findEvenIndex(new int[] {1,2,3,4,3,2,1});
		findEvenIndex(new int[] {1,2,3,4,5,6});
		
	}
	
	public static int findEvenIndex(int[] arr) {
		
		int left = 0;
		int right = Arrays.stream(arr).sum();
		System.out.println("Sum of elements in array are: " + right);
		
		int idx = 0;
		
		for(int i=0; i<arr.length; i++) {
			right -= arr[i];
			System.out.println("Current value of right after subtraction = " + right);
			System.out.println("Current value of left before comparison =  " + left);
			
			if(left == right) {
				System.out.println("=======================================");
				System.out.println("Right and Left are the same at index = " + i);
				System.out.println("=======================================");
				return i;
			}
			
			left += arr[i];
		}
		
		return -1;
		
	}
	
	

}
