fn main() {
    let name="Andrew";
    println!("Hello, {name}", );


    let my_array: [i32; 5] = [1, 2, 3, 4, 5];
    let my_tuple= (2, "hi", 3.14);

    println!("{:?},\n{:?}",
    my_tuple,
    my_array
            );

    println!("{0}, {1} {0}", my_array[0] , my_tuple.1);
    println!("{:#?},\n{:#?}",
    my_tuple,
    my_array
            );

    for i in 0..my_array.len() {
        println!("{}", i);
    }

    println!("{:?}", my_array);
    for item in my_array.iter() {
        println!("{}", item);
    }
}
