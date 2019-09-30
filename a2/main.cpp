/*
Simple genetic algorithm to determine black box fitness 
*/
#include <iostream>
#include <random>

using namespace std;

const static int NUM_AGENT = 100;

// expects pointer to integer array of length 100, where each element is either 0 or 1
double eval(int *pj);

void make_random_vec(int v[150], int size) {
  // random number generation
  random_device rd;
  mt19937 rng(rd());
  uniform_int_distribution<int> uni_dist(0, 1);

  int bit_val = 0;
  for( int i = 0; i < size; i++ ){
    bit_val = uni_dist(rng);
    v[i] = bit_val;
  }
  return;
}

void sample_new_population(double fitness[NUM_AGENT], int fit_size, int v[NUM_AGENT][150],
    int row, int col){

  // get total fitness
  double fit_sum[fit_size];
  for( int i = 0; i < fit_size; i++ ){
    if( i == 0 ){
      fit_sum[i] = fitness[0];
    } else {
      fit_sum[i] = fitness[i] + fit_sum[i-1];
    }
  }
  int fit_total = int(fit_sum[fit_size-1]);

  // random number generation
  random_device rd;
  mt19937 rng(rd());
  uniform_int_distribution<int> uni_dist(0, fit_total-1);
  int rand_num = 0;

  // get new memebers of population via roulette wheel
  int new_pop_idx[fit_size];
  for( int i = 0; i < fit_size; i ++ )
  {
    new_pop_idx[i] = 0;
  }
  
  for( int i = 0; i < fit_size; i++ ){    
    rand_num = uni_dist(rng);

    int idx = 0;
    while( idx < fit_size ) {
      if( idx == 0 ) {
        if( rand_num < fit_sum[idx] ) {
          new_pop_idx[i] = idx;
          idx = fit_size;
        }
      } else if( rand_num < fit_sum[idx] && rand_num > fit_sum[idx-1] ) {
        new_pop_idx[i] = idx;
        idx = fit_size;
      }
      idx += 1;
    }
  }

  // update population based on random selection above
  int new_pop[NUM_AGENT][150];
  for( int i = 0; i < fit_size; i++ ){
    for( int j = 0; j < 150; j++ ){
      new_pop[i][j] = v[new_pop_idx[i]][j];
    }
  }

  // copy back into original populations
  for( int i = 0; i < fit_size; i++ ){
    for( int j = 0; j < 150; j++ ){
      v[i][j] = new_pop[i][j];
    }
  }
  return;
}

void mutate(int v[NUM_AGENT][150], int row, int col){
  random_device rd;
  mt19937 rng(rd());
  // bounds on this distribution determine mutation probability
  uniform_int_distribution<int> uni_dist(0, 1000);
  int mutation_prob = 0;

  for( int i = 0; i < NUM_AGENT; i++ ){
    for( int j = 0; j < 150; j++ ){
      mutation_prob = uni_dist(rng);
      if( mutation_prob == 1 ){
        if( v[i][j] == 1 ) {
          v[i][j] = 0;
        } else {
          v[i][j] = 1;
        }
      }
    }
  }
  return;
}

void crossover(int v[NUM_AGENT][150], int row, int col) {
  random_device rd;
  mt19937 rng(rd());
  uniform_int_distribution<int> uni_dist_partner(0, 9);
  uniform_int_distribution<int> uni_dist_crossover_location(0, 99);
  int partner_idx = 0;
  int crossover_idx = 0;

  int new_pop[NUM_AGENT][150];
  for( int i = 0; i < NUM_AGENT; i++ ) {
    partner_idx = uni_dist_partner(rng);
    crossover_idx = uni_dist_crossover_location(rng);
    for( int j = 0; j < 150; j++ ) {
      if( j < crossover_idx ) {
        new_pop[i][j] = v[i][j];
      } else {
        new_pop[i][j] = v[partner_idx][j];
      }
    }

  }

  // new population -> original population array
  for( int i = 0; i < NUM_AGENT; i++ ){
    for( int j = 0; j < 150; j++ ){
      v[i][j] = new_pop[i][j];
    }
  }
  return;
}

void ga_basic(){
  // random number generation
  random_device rd;
  mt19937 rng(rd());
  uniform_int_distribution<int> uni_dist(0, 99);
  int idx = 0;

  int num_agent = NUM_AGENT; 
  int vec_size = 150;

  double fit[num_agent];
  double new_fit[num_agent];
  double scaled_fit[NUM_AGENT];
  int vecs[NUM_AGENT][150];

  // initialize relevant arrays
  for( int i = 0; i < num_agent; i++ ){
    fit[i] = 0;
    new_fit[i] = 0;
    scaled_fit[i] = 0;
    make_random_vec(vecs[i], 150);
  }

  int max_gen = 2000;
  int t = 0;
  while( t < max_gen ){
    // get fitness of current generation
    for( int i = 0; i < num_agent; i++ ){
      new_fit[i] = eval(vecs[i]);

      double max_fit = 0;
      for(int j = 0; j < NUM_AGENT; j++ ) {
        if( new_fit[j] > max_fit ){ 
          max_fit = new_fit[j];
        }
      }

      if(new_fit[i] != 32 ){
        cout << new_fit[i] << endl;
      }
      if( new_fit[i] == 64 ){
        cout << "FOUND MAX" << endl;
        cout << "total generations: " << t << endl;
        for(int j = 0; j < vec_size; j++ ){
          cout << vecs[i][j] << ", ";
        }
        return;
      }
      if( new_fit[i] == max_fit ) {
        scaled_fit[i] = new_fit[i] * 1.8;
      } else {
        scaled_fit[i] = new_fit[i];
      }
    }

    // roulette-style population upate
    // sample_new_population(new_fit, num_agent, vecs, NUM_AGENT, 150);
    sample_new_population(scaled_fit, num_agent, vecs, NUM_AGENT, 150);

    // mutation
    mutate(vecs, NUM_AGENT, 150);

    // crossover
    crossover(vecs, NUM_AGENT, 150);
    t++;
  }

  for( int i = 0; i < num_agent; i++ ){
    cout << endl;
    for(int j = 0; j < vec_size; j++ ){
      cout << vecs[i][j] << ", ";
    }
  }
}

int main() {
  // 1
  // random_hill_climb();

  // 2
  ga_basic();
  return 0;
}
