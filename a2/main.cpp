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
  int vec[150];
  for(int i = 0; i < 150; i++){
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