#include <bits\stdc++.h>
using namespace std;

unordered_set<int> alps;        // alphabet
unordered_map<int, int> occ;    // occurrence function
unordered_set<int> getAlphabet(string s);   // get alphabet from string
bool processBadCharacters(string p, int m); // preprocessing bad characters
void processGoodSuffixesCase01(string p, int m, int bpos[], int shift[]);
void processGoodSuffixesCase01(int m, int bpos[], int shift[]);


/*
 * Algorithm: Boyer-Moore
 * Author: Oreder
 * Language: cpp
 * Complexity: O(m + |Σ|)
 * Inputs: t - text, p - pattern to match
 */
void search(string t, string p) {
    int n = t.length(),
        m = p.length();
    
    // SPECIAL CASE: pattern is empty or longer than text
    if (m == 0 || m > n) {
        cout << "Pattern is not found!\n";
        return;
    }

    // Bad characters processing
    alps = getAlphabet(t);
    if (!processBadCharacters(p, m)) {
        cout << "Pattern is not found!\n";
        return;
    }

    int bpos[m + 1], shift[m + 1];

    // Initializing all occurrence of shift to 0
	for(int i = 0; i < m + 1; i++)
		shift[i] = 0;

    // Good suffixes processing
    processGoodSuffixesCase01(p, m, bpos, shift);
    processGoodSuffixesCase02(m, bpos, shift);

    int i = 0,      // shift of the pattern with respect to text
        total = 0;  // matched pattern counter
    while (i <= n - m) {
        int j = m - 1;
        /* Keep reducing index j of pattern while characters of 
		 * pattern and text are matching at this shift s */
        while (j >= 0 && p[j] == t[i + j])
            j--;
        
        /* If the pattern is present at the current shift, then index j 
		 * will become -1 after the above loop */
        if (j < 0) {
            cout << "Pattern is found at index " <<  i << endl;
            total++;
            i += shift[0];
        } else {
            /* pat[i] != pat[s+j] so shift the pattern shift[j+1] times */
            i += shift[j + 1];
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

unordered_set<int> getAlphabet(string s) {
    unordered_set<int> alps;
    for (int c: s) {
        if (alps.find(c) == alps.end())
            alps.insert(c);
    }
    return alps;
}

bool processBadCharacters(string p, int m) {
    for (int i = 0; i < m; i++) {
        if (alps.find(p[i]) == alps.end())
            return false;
        occ[p[i]] = i;
    }
    return true;
}

void processGoodSuffixesCase01(string p, int m, int bpos[], int shift[]) {
    int i = m,
        j = m + 1;
        bpos[i] = j;
    while (i > 0) {
        /* if character at position i-1 is not equivalent to 
		 * character at j-1, then continue searching to right 
		 * of the pattern for border */
        while (j <= m && p[i - 1] != p[j - 1]) {
            /* the character preceding the occurrence of t in 
			 * pattern P is different than the mismatching character in P, 
			 * we stop skipping the occurrences and shift the pattern from i to j */
            if (shift[j] == 0)
                shift[j] = j - i;

            // Update the position of next border
            j = bpos[j];
        }
        i--;
        j--;
        bpos[i] = j;
    }
}

void processGoodSuffixesCase02(int m, int bpos[], int shift[]) {
    for (int i = 0, j = bpos[0]; i <= m; i++) {
        /* set the border position of the first character of the pattern 
		 * to all indices in array shift having shift[i] = 0 */
        if (shift[i] == 0)
            shift[i] = j;

        /* suffix becomes shorter than bpos[0], use the position of 
		 * next widest border as value of j */
        if (i == j)
            j = bpos[j];
    }
}