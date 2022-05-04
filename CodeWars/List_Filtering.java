// LINK: https://www.codewars.com/kata/53dbd5315a3c69eed20002dd/train/java

package me.mary.jonah;

import java.util.ArrayList;
import java.util.List;

public class List_Filtering {

    public static void main(String[] args) {
	// write your code here
        System.out.println(filterList(List.of(1, 2, "a", "b")));
    }
    public static List<Object> filterList(final List<Object> list) {
        // Return the List with the Strings filtered out
        List<Object> resultNum = new ArrayList<>();
        for (Object obj : list){
            if (obj instanceof Integer) {
                resultNum.add(obj);
            }
        }
        return resultNum;
    }
}
