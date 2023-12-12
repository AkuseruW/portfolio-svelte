import { SERVEUR_URL } from '$env/static/private';
import type { Actions } from './$types';


export const actions: Actions = {
    login: async ({ request, cookies }) => {
        const formData = await request.formData();

        const data = {
            email: formData.get('email'),
            password: formData.get('password'),
        }

        const res = await fetch(`${SERVEUR_URL}/api/login/`, {
            headers: {
                'Content-Type': 'application/json'
            },
            method: 'POST',
            body: JSON.stringify(data),
        })

        if ( res.ok ) {
            
            const json = await res.json();
            console.log(json)
            cookies.set('access_token', json.access_token, {
                path: '/',
                httpOnly: true
            });
        }
        
        return { success: true };
    }

}