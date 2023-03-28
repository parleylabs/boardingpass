import { observable, runInAction } from 'mobx'
import ApiService from '../services/ApiService'
import StorageService from '../services/StorageService'
import history from '../services/history'

class AuthStore {
    loginSession = observable({
        isAuthenticated: false,
        isLoading: true,
        isFailure: false,
        currentUser: null,
        profileErrors: null,
        login: async (params) => {
            try {
                const res = await ApiService.login(params)
                StorageService.setToken(res.key)
                runInAction(() => {
                    this.loginSession.isAuthenticated = true
                    this.loginSession.isFailure = false
                    this.loginSession.isLoading = false
                })
            } catch (e) {
                runInAction(() => {
                    this.loginSession.isAuthenticated = false
                    this.loginSession.isFailure = true
                    this.loginSession.isLoading = false
                })
            }
        },
        logout: async () => {
            await ApiService.logout(StorageService.getToken())
            StorageService.removeToken()
            runInAction(() => {
                this.loginSession.isAuthenticated = false
                this.loginSession.isFailure = false
                this.loginSession.currentUser = null
                this.loginSession.isLoading = false
                history.push('/')
            })
        }
    });
}

export default new AuthStore()
export { AuthStore }