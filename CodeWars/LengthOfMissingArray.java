package com.codewars.katas.collections;

import java.util.Arrays;

public class LengthOfMissingArray {

	public static void main(String[] args) {
		System.out.println(getLengthOfMissingArray(new Object[][] { new Object[] { 1, 2 }, new Object[] { 4, 5, 1, 1 }, new Object[] { 1 }, new Object[] { 5, 6, 7, 8, 9 }} ));        
        System.out.println(getLengthOfMissingArray(new Object[][] { new Object[] { 5, 2, 9 }, new Object[] { 4, 5, 1, 1 }, new Object[] { 1 }, new Object[] { 5, 6, 7, 8, 9 }} ));
        System.out.println(getLengthOfMissingArray(new Object[][] { new Object[] { null }, new Object[] { null, null, null } } ));
        System.out.println(getLengthOfMissingArray(new Object[][] { new Object[] { 'a', 'a', 'a' }, new Object[] { 'a', 'a' }, new Object[] { 'a', 'a', 'a', 'a' }, new Object[] { 'a' }, new Object[] { 'a', 'a', 'a', 'a', 'a', 'a' }} ));		
	}

	
	public static int getLengthOfMissingArray(Object[][] arrayOfArrays) {
		if(arrayOfArrays == null || arrayOfArrays.length == 0) {
			return 0;
		}
		int[] arrayOfSizes = new int[arrayOfArrays.length];
		
		for(int i=0; i < arrayOfArrays.length; i++) {
			if(arrayOfArrays[i] == null || arrayOfArrays[i].length == 0) {
				return 0;
			}
			
			arrayOfSizes[i] = arrayOfArrays[i].length;
		}
		
		Arrays.sort(arrayOfSizes);
		
		for(int i=0; i<arrayOfSizes.length - 1; i++) {
			if(arrayOfSizes[i+1] - arrayOfSizes[i] - 1 != 0) {
				return arrayOfSizes[i] + 1;
			}
		}
			
		return 0;
	}
}
