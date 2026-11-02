import { useState } from 'react';
import { TextInput, Button, View } from 'react-native';
import { supabase } from '../App';

export default function ManDangNhap() {
  const [email, setEmail] = useState('');
  const [matKhau, setMatKhau] = useState('');
  const dangNhap = () => supabase.auth.signInWithPassword({ email, password: matKhau });
  return (
    <View>
      <TextInput keyboardType="email-address" value={email} onChangeText={setEmail} placeholder="Email" />
      <TextInput secureTextEntry value={matKhau} onChangeText={setMatKhau} placeholder="Mật khẩu" />
      <Button title="Đăng nhập" onPress={dangNhap} />
    </View>
  );
}
