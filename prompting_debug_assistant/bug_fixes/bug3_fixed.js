function getUserAge(user) {
    if (!user.profile) {  // düzəliş: undefined yoxlanır
        return "Profile not found";
    }
    return user.profile.age;
}

// Test
const user1 = { name: "Ali", profile: { age: 25 } };
const user2 = { name: "Aysel" };

console.log(getUserAge(user1));  // 25 ✅
console.log(getUserAge(user2));  // "Profile not found" ✅
