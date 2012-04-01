/**
 * Created with IntelliJ IDEA.
 * User: kroot
 * Date: 4/1/12
 * Time: 4:55 PM
 * To change this template use File | Settings | File Templates.
 */
import java.util.Scanner;

public class QuickSort {
    public static void main(String[] args) {
        int[] numbers1 = new int[10000];
        int[] numbers2 = new int[10000];
        int[] numbers3 = new int[10000];

        Scanner scanner = new Scanner(QuickSort.class.getResourceAsStream("QuickSort.txt"));
        int     i = 0;
        for (; i < numbers1.length; i++) {
            numbers1[i] = Integer.parseInt(scanner.nextLine());
        }

        System.arraycopy(numbers1, 0, numbers2, 0, numbers1.length);
        System.arraycopy(numbers1, 0, numbers3, 0, numbers1.length);

        long comparisons1 = partitionFromFirstElement(numbers1, 0, numbers1.length-1);
        System.out.println("Pivot = first item, comparisons total = " + comparisons1);
        verifySortedArray(numbers1, false);

        long comparisons2 = partitionFromLastElement(numbers2, 0, numbers2.length-1);
        System.out.println("Pivot = last item, comparisons total = " + comparisons2);
        verifySortedArray(numbers2, false);
    }

    private static void verifySortedArray(int[] array, boolean printValues) {
        if (printValues) {
            for (int i = 0; i < array.length; i++) {
                System.out.println(array[i]);
            }
        }

        System.out.print("Verifying sorting: ...");
        boolean ok = true;
        for (int i = 1; i < array.length; i++) {
            if (array[i] <= array[i-1]) {
                ok = false;
                System.out.println(" failed at position i = " + i + "!");
            }
        }
        if (ok) {
            System.out.println(" succeeded!");
        }
    }

    private static void swap (int[] array, int index1, int index2) {
        int temp = array[index1];
        array[index1] = array[index2];
        array[index2] = temp;
    }

    private static long partitionFromFirstElement(int[] array, int start, int end) {
        if (((end - start) < 1) || (start > end)) {
            return 0;
        }

        int partitionValue = array[start];
        int i = start + 1;

        for (int j = start + 1; j <= end; j++) {
            if (array[j] < partitionValue) {
                swap(array, j, i);
                i++;
            }
        }

        swap(array, start, i-1);

        long numberOfComparisons = end - start;
        numberOfComparisons += partitionFromFirstElement(array, start, i-2);
        numberOfComparisons += partitionFromFirstElement(array, i, end);

        return numberOfComparisons;
    }

    private static long partitionFromLastElement(int[] array, int start, int end) {
        if (((end - start) < 1) || (start > end)) {
            return 0;
        }

        swap(array, start, end);

        int partitionValue = array[start];
        int i = start + 1;

        for (int j = start + 1; j <= end; j++) {
            if (array[j] < partitionValue) {
                swap(array, j, i);
                i++;
            }
        }

        swap(array, start, i-1);

        long numberOfComparisons = end - start;
        numberOfComparisons += partitionFromLastElement(array, start, i-2);
        numberOfComparisons += partitionFromLastElement(array, i, end);

        return numberOfComparisons;
    }
//
//    private static long partitionFromLastElement_incorrect(int[] array, int start, int end) {
//        if (((end - start) < 1) || (start > end)) {
//            return 0;
//        }
//
//        int partitionValue = array[end];
//        int i = start;
//
//        for (int j = start; j < end; j++) {
//            if (array[j] < partitionValue) {
//                swap(array, j, i);
//                i++;
//            }
//        }
//
//        swap(array, end, i);
//
//        long numberOfComparisons = end - start;
//        numberOfComparisons += partitionFromLastElement(array, start, i-1);
//        numberOfComparisons += partitionFromLastElement(array, i+1, end);
//
//        return numberOfComparisons;
//    }
}