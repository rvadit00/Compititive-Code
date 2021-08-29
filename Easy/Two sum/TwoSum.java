class Solution {
    public int[] twoSum(int[] nums, int target) {
       
        int i,j;
        for(i =0;i<nums.length-1;i++)
        {
            for(j=1;j<nums.length;j++)
            {
                int[] a= new int[1];
                if(nums[i]+nums[j]==target)
                {
                     
                    a[0]=i;
                    a[1]=j;
                    System.out.println(i);
                    return a; 
                }else 
                {
                    return a;
                }
            }
        }
    }
}