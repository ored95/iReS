#include <bits\stdc++.h>
using namespace std;
#define NCHARS 256

int getNextState(string p, int m, int state, char x);
void preprocessing(string p, int m, int TF[][NCHARS]);

/*
 * Algorithm: Finite automaton matcher
 * Author: Oreder
 * Language: cpp
 * Complexity: O(n + m|Σ|)
 * Inputs: t - text, p - pattern to match
 */
void search(string t, string p) {
    int n = t.size(),
        m = p.size();
    
    // SPECIAL CASE: pattern is empty or longer than text
    if (m == 0 || m > n) {
        cout << "Pattern is not found!\n";
        return;
    }    
    
    int total = 0;
    int TF[m + 1][NCHARS];
    preprocessing(p, m, TF);

    int state = 0;
    for (int i = 0; i < n; i++) {
        state = TF[state][t[i]];
        if (m == state) {
            cout << "Pattern is found at index " << i - m + 1 << endl;
            total++;
        }
    }

    if (total == 0)
        cout << "Pattern is not found!\n";
}

int main() {
    string text, pattern;
    cin >> text >> pattern;

    search(text, pattern);
    return 0;
}

// delta(x): the longest prefix which is also suffix in "p[0..state-1]x"
int getNextState(string p, int m, int state, int x) {
    if (state < m && p[state] == x)
        return state + 1;

    for (int ns = state; ns > 0; ns--) {
        int N = ns - 1;
        if (p[N] == x) {
            int i = 0;
            while(i < N && p[i] == p[state - N + i])
                i++;
            if (i == N)
                return ns;
        }
    }
    return 0;   // no matching
}

void preprocessing(string p, int m, int TF[][NCHARS]) {
    for (int state = 0; state <= m; state++) {
        for (int x = 0; x < NCHARS; x++) {
            TF[state][x] = getNextState(p, m, state, x);
        }
    }
}