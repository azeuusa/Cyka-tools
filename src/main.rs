use std::process::Command;
use std::io;
use rand::Rng;


fn main() {

  let angka = rand::thread_rng().gen_range(1..=10);

  loop {
      
  
  println!("tebak angka 1 -> 10");

  let mut input = String::new();
  
  

  io::stdin()
  .read_line(&mut input)
  .expect("gagal read jit");

  let tebakan: u32 = match input.trim().parse() {

    Ok(anga) => anga,
    Err(_) => continue
  };


  

  if tebakan == angka {

    println!("kamu bener");
      
  }

  else {

    Command::new("sh")
    .arg("-c")
    .arg("kitty")
    .output()
    .expect("kanyut");
    break;
  }

  



  
    
  

   }

    
}
