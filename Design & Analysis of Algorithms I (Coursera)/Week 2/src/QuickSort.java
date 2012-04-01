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

        partitionFromFirstElement(numbers1, 0, numbers1.length-1);
        verifySortedArray(numbers1, false);

        partitionFromLastElement(numbers2, 0, numbers2.length-1);
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

    private static void partitionFromFirstElement(int[] array, int start, int end) {
        if (((end - start) < 1) || (start > end)) {
//            System.out.println("start = " + start + ", end = " + end);
            return;
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

        partitionFromFirstElement(array, start, i-2);
        partitionFromFirstElement(array, i, end);

        return;
    }

    private static void partitionFromLastElement(int[] array, int start, int end) {
        if (((end - start) < 1) || (start > end)) {
//            System.out.println("start = " + start + ", end = " + end);
            return;
        }

        int partitionValue = array[end];
        int i = start;

        for (int j = start; j < end; j++) {
            if (array[j] < partitionValue) {
                swap(array, j, i);
                i++;
            }
        }

        swap(array, end, i);

        partitionFromFirstElement(array, start, i-1);
        partitionFromFirstElement(array, i+1, end);

        return;
    }
}
