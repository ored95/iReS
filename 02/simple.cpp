#include <bits\stdc++.h>
using namespace std;

/*
 * Algorithm: Naive String Matcher
 * Author: Oreder
 * Language: cpp
 * Complexity: O((n-m+1)*m)
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
    for (int i = 0; i <= n - m; ++i) {
        int j = 0;
        while (j < m && t[i + j] == p[j])
            ++j;
        if (j == m) {
            cout << "Pattern is found at index " << i << endl;
            total++;;
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