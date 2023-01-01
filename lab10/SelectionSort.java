//Simple implementation of Selection Sort in Java

import java.util.Random;
import java.util.Arrays;

public class SelectionSort {

  public static int[] selectionSort(int[] values){
    // Compute length of array
    int size = values.length;

    // TODO: Traverse through all array elements

          // TODO: Find the minimum element in i + 1 onwards

          // TODO: Swap the found min element with ith element

    return values;
  }

  public static void main(String args[]) {
    int size = 10;
    int randArray[] = new int[size];
    Random r = new Random();

    // Populate array with random numbers
    for (int i = 0; i < size; i++) {
      // nextInt(n) returns random number in the range [0,n)
      randArray[i] = r.nextInt(100);
    }

    System.out.println("Array before sorting:");
    // TODO: Print unsorted array (randArray)

    // TODO: Call selection sorting method

    System.out.println("Sorted array:");
    // TODO: Print sorted array returned by selection sort

  } //end main method
} // end class
