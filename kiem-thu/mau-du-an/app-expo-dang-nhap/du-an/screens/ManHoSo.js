import { Button, View, Text } from 'react-native';
import { CameraView } from 'expo-camera';
import { supabase } from '../App';

export default function ManHoSo() {
  return (
    <View>
      <Text>Hồ sơ của bạn</Text>
      <CameraView style={{ height: 200 }} />
      <Button title="Đăng xuất" onPress={() => supabase.auth.signOut()} />
    </View>
  );
}
