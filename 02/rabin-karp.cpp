#include <bits\stdc++.h>
#include <cstdlib>
using namespace std;

/*
 * Algorithm: Rabin Karp Matcher
 * Author: Oreder
 * Language: cpp
 * Complexity: O(n + m)
 * Inputs:  t - text, 
 *          p - pattern to match,
 *          d - number of characters in the alphabet,
 *          q - a prime number.
 */
void search(string t, string p, int q, int d = 256) {
    int n = t.size(),
        m = p.size();
    
    // SPECIAL CASE: Length of pattern is smaller than 2 or longer than text
    if (m == 0 || m > n) {
        cout << "Pattern is not found!\n";
        return;
    }

    // algorithm works if only pattern is not longer than text
    cout << "$ d=" << d << ", q=" << q << endl; 
    int i, h = 1;
    for (i = 1; i < m; ++i) {
        h = (h * d) % q;
    }
    
    // calculate hash(pattern)
    int hp = 0, ht = 0;
    for (i = 0; i < m; ++i) {
        hp = (d * hp + p[i]) % q;
        ht = (d * ht + t[i]) % q;
    }
    
    // slide the pattern over text one by one
    int total = 0;
    for (i = 0; i <= n - m; ++i) {
        if (hp == ht) {
            int j = 0;
            while (j < m && t[i + j] == p[j])
                ++j;
            if (j == m) {
                cout << "Pattern is found at index " << i << endl;
                total++;
            }
        }

        if (i < n - m) {
            ht = (d * (ht - t[i] * h) + t[i + m]) % q;

            if (ht < 0)     // we might get negative value
                ht += q;
        }
    }
    if (total == 0)
        cout << "Pattern is not found!\n";
}

// return the random prime number in range [2..d]
int getPrimeNumber(int d = 256) {
    vector<int> primes;
    primes.push_back(2);
    for (int n = 3; n <= d; ++n) {
        bool match = true;
        for (int x: primes) {
            if (n % x == 0) {
                match = false;
                break;
            }
        }
        if (match)
            primes.push_back(n);
    }
    return primes.at((int)(rand() % primes.size()));
}

int main() {
    string src, sub;
    int d = 256;
    cin >> src >> sub;
    int q = getPrimeNumber(d);

    search(src, sub, q, d);
    return 0;
}