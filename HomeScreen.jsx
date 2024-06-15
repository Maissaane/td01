import React from 'react';
import { View, Text, TouchableOpacity, StyleSheet, TextInput, Linking } from 'react-native';

const HomeScreen = () => {
  const handlePress = (socialMedia) => {
    // Gérer la redirection vers le réseau social sélectionné
    switch (socialMedia) {
      case 'facebook':
        Linking.openURL('https://www.facebook.com');
        break;
      case 'twitter':
        Linking.openURL('https://www.twitter.com');
        break;
      case 'instagram':
        Linking.openURL('https://www.instagram.com');
        break;
      default:
        break;
    }
  };

  return (
    <View style={styles.container}>
      <Text style={styles.title}>Bienvenue sur l'application</Text>
      
      <View style={styles.linkContainer}>
        <Text style={styles.linkText}>Visitez notre site web :</Text>
        <TouchableOpacity onPress={() => Linking.openURL('https://www.example.com')}>
          <Text style={styles.websiteLink}>www.example.com</Text>
        </TouchableOpacity>
      </View>
      <TextInput
        style={styles.input}
        placeholder="Entrez votre adresse email"
        keyboardType="email-address"
      />
      <View style={styles.buttonContainer}>
        <TouchableOpacity
          style={styles.button}
          onPress={() => handlePress('facebook')}
        >
          <Text style={styles.buttonText}>Facebook</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.button}
          onPress={() => handlePress('twitter')}
        >
          <Text style={styles.buttonText}>Twitter</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={styles.button}
          onPress={() => handlePress('instagram')}
        >
          <Text style={styles.buttonText}>Instagram</Text>
        </TouchableOpacity>
      </View>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
    backgroundColor: '#fff',
  },
  title: {
    fontSize: 24,
    marginBottom: 20,
  },
  buttonContainer: {
    flexDirection: 'row',
    marginTop: 'auto',
    marginHorizontal: 20
  },
  button: {
    backgroundColor: '#007bff',
    paddingVertical: 15,
    paddingHorizontal: 30,
    marginHorizontal: 10,
    borderRadius: 5,
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
  },
  linkContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    marginBottom: 10,
  },
  linkText: {
    fontSize: 16,
    marginRight: 10,
  },
  websiteLink: {
    fontSize: 16,
    color: '#007bff',
    textDecorationLine: 'underline',
  },
  input: {
    width: '80%',
    height: 40,
    borderColor: 'gray',
    borderWidth: 1,
    paddingHorizontal: 10,
    borderRadius: 5,
  },
});

export default HomeScreen;
