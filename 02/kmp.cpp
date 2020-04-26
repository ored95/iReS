#include <bits\stdc++.h>
using namespace std;

void computePrefixFunction(string p, int m, int lps[]);

/*
 * Algorithm: Knuth–Morris–Pratt
 * Author: Oreder
 * Language: cpp
 * Complexity: O(m + n)
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
    int lps[m];
    computePrefixFunction(p, m, lps);

    int i = 0; 
    int j = 0; 
    while (i < n) { 
        if (p[j] == t[i]) { 
            j++;
            i++;
        }

        if (j == m) { 
            cout << "Pattern is found at index " << i - m << endl;
            total++;
            j = lps[j - 1]; 
        } 
  
        // mismatch after j matches
        else if (i < n && p[j] != t[i]) { 
            // Do not match lps[0..lps[j-1]] characters, they will match anyway 
            if (j != 0)
                j = lps[j - 1];
            else
                i++; 
        }
    }
    if (total == 0)
        cout << "Pattern is not found!\n";
}

// VERSION 2 (in case of '#' is NOT in alphabet of s and t)
void search_quick(string t, string p) {
    int n = t.size(), 
        m = p.size();
    
    // SPECIAL CASE: pattern is empty or longer than text
    if (m == 0 || m > n) {
        cout << "Pattern is not found!\n";
        return;
    }

    int total = 0;
    int lps[m + n + 1];
    computePrefixFunction(p + "#" + t, m + n + 1, lps);

    for (int i = 0; i < m + n + 1; i++)
        cout << lps[i] << " ";
    cout << endl;

    for (int i = 0; i < n; i++) {
        if (lps[i + m + 1] == m) {
            cout << "Pattern is found at index " << i - m + 1 << endl;
            total++;
        }
    }
    if (total == 0)
        cout << "String " << p << " is not found in " << t << endl;
}

int main() {
    string text, pattern;
    cin >> text >> pattern;

    search(text, pattern);
    return 0;
}

void computePrefixFunction(string p, int m, int lps[]) {
    lps[0] = 0;  // by default
    int k = 0;
    for (int i = 1; i < m; i++) {
        k = lps[i - 1];
        while (k > 0 && p[i] != p[k])
            k = lps[k - 1];
        if (p[i] == p[k])
            k++;
        lps[i] = k;
    }
}