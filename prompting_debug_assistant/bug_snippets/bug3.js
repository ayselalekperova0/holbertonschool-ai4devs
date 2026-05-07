function getUserAge(user) {
    return user.profile.age;  // bug: user.profile undefined ola bilər
}

const user1 = { name: "Ali", profile: { age: 25 } };
const user2 = { name: "Nərmin" };

console.log(getUserAge(user1));  // 25 ✅
console.log(getUserAge(user2));  // Error: Cannot read properties of undefined
