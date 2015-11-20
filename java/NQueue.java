/**
 * 回溯法-八皇后
 * Created by devin on 15-11-13.
 */
public class NQueue {
    private int[] X;
    private int n;//皇后的个数

    /**
     * 初始化
     * @param n : give n queues
     */
    public NQueue(int n){
        this.n = n;
        this.X = new int[n];
    }

    public int[] getX() {
        return X;
    }

    /**
     * 讲第k个皇后放在第k列
     * @param k
     * @return true or false
     */
    private boolean place(int k){
        int i=0;
        while(i<k) {
            if (X[i] == X[k] || Math.abs(X[i] - X[k]) == Math.abs(i - k)) {
                return false;
            }
            i++;
        }
        return true;
    }

    public void solve(){
        X[0] = -1; //第一个皇后再第0列
        int k = 0; //从第0行开始,x[k]表示当前列
        while(k >= 0){
            X[k] = X[k] + 1;
            while(X[k] <= n-1 && place(k) == false){
                X[k] += 1; //增加一列
            }
            if(X[k] <= n-1){
                if(k == n-1) {
                    return;
                }else{
                    k += 1;
                    X[k] = -1;//从第0列开始
                }
            }else{
                k -= 1;//回溯
            }
        }
    }

}
