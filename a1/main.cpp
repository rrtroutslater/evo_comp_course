/*
Hill climbing to determine max of "black box" fitness function
*/
#include <iostream>
#include <random>

using namespace std;

// expects pointer to integer array of length 100, where each element is either 0 or 1
double eval(int *pj);

void flip_bit(int * guess, int idx) {
  // flips a single specified bit
  if(guess[idx] == 1) {
    guess[idx] = 0;
  } else {
    guess[idx] = 1;
  }
  return;
}

// check whether a number is prime
bool check_prime(int n) {
  if ( n == 0 || n == 1 ) {
    return false;
  }
  int i = 2;
  while (i <= float(n/2)) {
    if ( n % i == 0 ){
      return false;
    }
    i ++;
  }
  return true;
}

// eval function for problem 1
double eval_rr(int v[100], int size){
  // 10 score points for every prime index which is set to 1
  double score = 0;
  int ctr = 0;
  for (int i = 0; i < size; i++) {
    if (v[i] == 1 && check_prime(i)) {
      score += 10;
    } else if (v[i] == 1) {
      // -0.5 point for every non-prime index set to 1
      score -= 0.3;
    }
    if (v[i] == 1) {
      ctr += 1;
    }
  }
  if (ctr > 2 && ctr % 2 == 0) {
    // -9 points if an even number of ones in vector
    score -= 9;
  }
  return score;
}

void random_hill_climb(){
  /*
  simple random hill climber, flips one bit per iteration
  */

  // random number generation
  random_device rd;
  mt19937 rng(rd());
  uniform_int_distribution<int> uni_dist(0, 99);
  int idx = 0; 
  
  // initialize vector to all 0
  int vec[100];
  for(int i = 0; i < 100; i++){
    vec[i] = 0;
  }
  // double fitness = eval(vec);
  double fitness = 0;
  double new_fitness = 0;

  int ctr = 0;
  while(fitness != 250) {
    // get a new random index
    idx = uni_dist(rng);
    // modify bitstring 
    flip_bit(vec, idx);
    // new_fitness = eval(vec);
    new_fitness = eval_rr(vec, 100);

    // if new vector is worse, change it back
    if(new_fitness < fitness) {
      flip_bit(vec, idx);
    } else {
      fitness = new_fitness;
    }
    cout << "fitness = " << fitness << endl;
    ctr ++;
    cout << "counter = " << ctr << endl;
  }

  // print resulting array
  int sum = 0;
  for(int i = 0; i < 100; i++) {
    cout << vec[i] << ", ";
    sum += vec[i];
  }
  cout << endl;
  cout << sum << endl;
  return;
}

int main() {
  // 1
  random_hill_climb();

  // 2
  return 0;
}