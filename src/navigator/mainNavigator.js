import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import Maps191142Navigator from '../features/Maps191142/navigator';
import Additem191141Navigator from '../features/Additem191141/navigator';
import Maps191137Navigator from '../features/Maps191137/navigator';
import UserProfile191133Navigator from '../features/UserProfile191133/navigator';
import BlankScreen0191108Navigator from '../features/BlankScreen0191108/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
Maps191142: { screen: Maps191142Navigator },
Additem191141: { screen: Additem191141Navigator },
Maps191137: { screen: Maps191137Navigator },
UserProfile191133: { screen: UserProfile191133Navigator },
BlankScreen0191108: { screen: BlankScreen0191108Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
